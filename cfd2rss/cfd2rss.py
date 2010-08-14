#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

import datetime
import PyRSS2Gen

CLUB="Les Tire-Clous du Grand Mantis"
CLUB_URL="http://www.tire-clous.fr"

class Vol:
    def __init__(self, pilote, date, vtype, deco, aterro, distance):
        self.pilote = pilote
        self.vtype = vtype
        self.deco = deco
        self.aterro = aterro
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.link = None
        self.balises = None
        self.distance = distance

    def toRSSItem(self):
        return PyRSS2Gen.RSSItem(
            title = "{0} {1}km {2}".format(self.date.strftime("%d/%m/%y"), self.distance, self.pilote),
            link = self.link,
            description = str(self),
            guid = PyRSS2Gen.Guid(self.link),
            pubDate = self.date)
    
    def __repr__(self):
        s = """Vol de {0}, le {1}.
 - distance : {7}
 - deco: {2} / aterro: {3}
 - balises: {4}
 - type: {5}
 - link: {6}
""".format(self.pilote, self.date, self.deco, self.aterro, self.balises, self.vtype, self.link, self.distance)
        return s

balises_re=re.compile('href="(?P<gpshref>.*)">gps.*balises : (?P<balises>.*)</font></i></td>')
info_vol_re=re.compile('tous les vols du (?P<date>[^"]*)">.*</a></td><td><a href="(?=/pilote)(?P<pilotehref>[^"]*)">(?P<pilote>[^<]*)</a>.*type">(?P<type>[^<]*).*<td>(?P<deco>.*)</td><td>(?P<aterro>.*)</td><td align="right">(?P<distance>[^<]*)</td>')

fin = open(sys.argv[1])

all_vols=[]
cvol = None

for l in fin.xreadlines():
    m = info_vol_re.search(l)
    if m :
        cvol = Vol(m.group('pilote'), 
                   m.group('date'), 
                   m.group('type'), 
                   m.group('deco'), 
                   m.group('aterro'),
                   m.group('distance'))
        continue
    
    m = balises_re.search(l)
    if m:
        cvol.link = "http://parapente.ffvl.fr/"+m.group('gpshref')
        cvol.balises = m.group('balises')
        all_vols.append(cvol)
        cvol = None


rss = PyRSS2Gen.RSS2(
    title = "Vols CFD du club {0}".format(CLUB),
    link = CLUB_URL,
    description = "Les derniers vols déclarés à la CFD par le club {0}".format(CLUB),

    lastBuildDate = datetime.datetime.now(),

    items = [x.toRSSItem() for x in all_vols])

rss.write_xml(open("pyrss2gen.xml", "w"))



    
