#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Scripts for handling various aspects of my "Club"
#   Copyright (C) 2009  Marc Poulhiès
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from optparse import OptionParser

import cookielib, urllib2, urllib
from urllib2 import Request
import time
import datetime
import re
import os
import tempfile
from BeautifulSoup import BeautifulSoup

OVH_BASE_URL="https://www.ovh.com/"

OVH_LOGIN="/managerv3/login.pl"
OVH_ML_MANAGER="/managerv3/hosting-email-ml.pl"

OVH_SUBSCRIBER_XSLDOC='hosting/email/hosting-email-ml-subscriber-list.xsl'
OVH_SUBSCRIBER_DEL_XSLDOC='hosting/email/hosting-email-ml-subscriber-delete.xsl'
OVH_SUBSCRIBER_LIST_XSLDOC='hosting/email/hosting-email-ml-subscriber-list.xsl'
OVH_LOGIN_URL=OVH_BASE_URL+OVH_LOGIN
OVH_ML_MANAGER_URL=OVH_BASE_URL + OVH_ML_MANAGER

class OVHconnexion:
    def __init__(self, domain):
        self.domain = domain
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.cookie = None
        
    def connect(self, username, password):
        t = time.mktime(datetime.datetime.now().timetuple()) 


        data = urllib.urlencode({'ref': 'home.pl',
                                 'refxsl': '',
                                 'xsldoc': 'sub-login.xsl',
                                 'time': '%s' % t,
                                 'domain': '',
                                 'ajaxScn': '',
                                 'ticketId': '',
                                 'todo': 'Login',
                                 'session_nic': username,
                                 'session_password': password,
                                 'language': 'English'})

        print data
        r = self.opener.open(OVH_LOGIN_URL)

        try:
            req = Request(OVH_LOGIN_URL, data)
            handle = self.opener.open(req)

            for i in handle.readlines():
                m = re.search("Wrong user id or password", i)
                if m != None:
                    raise "Login failed"

            for index, cookie in enumerate(self.cj):
                self.cookie = "%s=%s" %(cookie.name, cookie.value)
                break # only one...!

            if self.cookie == None:
                raise "No cookie found, login failed"
                        
        except IOError, e:
            print 'Error opening "%s".' % theurl
            if hasattr(e, 'code'):
                print 'Error code - %s.' % e.code
            elif hasattr(e, 'reason'):
                print "Reason :", e.reason
                print "This usually means the server doesn't exist, is down, or we don't have an internet connection."
                raise "Error login with username [%s]" %username

    def get_ml_dict(self, xsldoc, ml, pos):
        data = {'language'   : 'fr',
                'domain'     : self.domain,
                'hostname'   : self.domain,
                'service'    : self.domain,
                'lastxsldoc' : 'hosting/email/hosting-email-ml.xsl',
                'csid'       : '0',
                'todo'       : '',
                'xsldoc'     : xsldoc,
                'associate'  : '',
                'email'      : '',
                'fieldtype'  : '',
                'filter'     : '',
                'ml'         : ml,
                'moderator'  : '',
                'pop'        : '',
                'position'   : pos,
                'priority'   : '',
                'redirected' : '',
                'responder'  : '',
                'subdomain'  : '',
                'target'     : ''
                }
        return data

    def get_mail_list(self, html):
        soup = BeautifulSoup(html)
        return [x.string for x in soup.findAll('td', attrs={'title': re.compile("^.*@.*$")})]
        
    def removeSubscribers(self, ml, subs):
        url = OVH_ML_MANAGER_URL
        (fd,path) = tempfile.mkstemp()
        tmpf = os.fdopen(fd, 'w')
        tmpf.write("\n".join(subs))
        tmpf.close()
        data = urllib.urlencode({'file': open(path, 'r'),
                                 'xsldoc': OVH_SUBSCRIBER_DEL_XSLDOC,
                                 'language'   : 'fr',
                                 'domain'     : self.domain,
                                 'hostname'   : self.domain,
                                 'service'    : self.domain,
                                 'lastxsldoc' :OVH_SUBSCRIBER_LIST_XSLDOC,
                                 'csid'       : '0',
                                 'email'      : '',
                                 'filter'     : '',
                                 'ml'         : ml,
                                 'pop'        : '',
                                 'position'   : '0',
                                 'redirected' : '',
                                 'subdomain'  : '',
                                 })

        r = urllib2.Request(OVH_ML_MANAGER_URL, data)
        handle = self.opener.open(r)
        os.unlink(path)
        lines = handle.readlines()
        for i in lines:
            print i,

    def getSubscribersList(self, ml):
        #ListAction('hosting/email/hosting-email-ml-subscriber-list.xsl','club.parapente','0')
        data = urllib.urlencode(self.get_ml_dict(OVH_SUBSCRIBER_XSLDOC, 
                                                 ml, 
                                                 '0'))
        r = urllib2.Request(OVH_ML_MANAGER_URL, data)
        handle = self.opener.open(r)

        return self.get_mail_list(handle.read())

    def publish(self):
        url = self.forge_url_base + "project/admin/publish.php"
        data = urllib.urlencode({'group_id'    : '27'})
        r = urllib2.Request(url, data)
        handle = self.opener.open(r)
        lines = handle.readlines()
        for i in lines:
            print i,

parser = OptionParser()

parser.add_option("-m", "--mailing-list",
                  help="Mailing list name", metavar="NAME")

parser.add_option("-a", "--add", metavar="FILENAME",
                  help="Add all mails from FILENAME to the list")

parser.add_option("-r", "--remove", metavar="FILENAME",
                  help="Remove all mails from FILENAME to the list")

parser.add_option("-s", "--set-to", metavar="FILENAME",
                  help="Set the list to contain only mails from FILENAME")

parser.add_option("-u", "--user", metavar="USERNAME",
                  help="username to use")

parser.add_option("-p", "--password", metavar="PASSWORD",
                  help="password to use")


(options, args) = parser.parse_args()

c = OVHconnexion(domain="tire-clous.fr")

c.connect(options.user, options.password)
current_subs = c.getSubscribersList(options.mailing_list)

if options.remove != None:
    f = open(options.remove)
    to_del = [x.strip() for x in f.readlines()]
    c.removeSubscribers(options.mailing_list, to_del)


# ListAction('hosting/email/hosting-email-ml-item-delete.xsl','club.parapente','')
# ListAction('hosting/email/hosting-email-ml-subscriber-list.xsl','club.parapente','0')
# ListAction('hosting/email/hosting-email-ml-moderator-list.xsl','club.parapente','0')
# ListAction('hosting/email/hosting-email-ml-item-modify.xsl','club.parapente','');

#mainPreLoad('hosting/email/hosting-email-ml-subscriber-delete.xsl'); 
#managerLoad ('/managerv3/hosting-email-ml.pl') ;
