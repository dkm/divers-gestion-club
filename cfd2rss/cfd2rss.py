#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

import datetime
import PyRSS2Gen

CLUB="Les Tire-Clous du Grand Mantis"
CLUB_URL="http://www.tire-clous.fr"

infile=sys.argv[1]
outfile=sys.argv[2]

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
            title = "%s %skm %s" %(self.date.strftime("%d/%m/%y"), self.distance, self.pilote),
            link = self.link,
            description = str(self),
            guid = PyRSS2Gen.Guid(self.link),
            pubDate = self.date)
    
    def __repr__(self):
        s = """Vol de %s, le %s.
 - distance : %s
 - deco: %s / aterro: %s
 - balises: %s
 - type: %s
 - link: %s
""" %(self.pilote, self.date, self.distance, self.deco, self.aterro, self.balises, self.vtype, self.link)
        return s

balises_re=re.compile('href="(?P<gpshref>.*)">gps.*balises : (?P<balises>.*)</font></i></td>')
info_vol_re=re.compile('tous les vols du (?P<date>[^"]*)">.*</a></td><td><a href="(?=/pilote)(?P<pilotehref>[^"]*)">(?P<pilote>[^<]*)</a>.*type">(?P<type>[^<]*).*<td>(?P<deco>.*)</td><td>(?P<aterro>.*)</td><td align="right">(?P<distance>[^<]*)</td>')

fin = open(infile)

all_vols=[]
cvol = None

for l in fin.xreadlines():
    l=l.decode('utf-8').encode("ascii", 'xmlcharrefreplace')
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
    title = "Vols CFD du club %s" %(CLUB),
    link = CLUB_URL,
    description = "Les derniers vols déclarés à la CFD par le club %s".decode('utf-8').encode("ascii", 'xmlcharrefreplace') %(CLUB),

    lastBuildDate = datetime.datetime.now(),

    items = [x.toRSSItem() for x in all_vols])

rss.write_xml(open(outfile, "w"))



    
