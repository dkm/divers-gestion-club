#!/usr/bin/env python

import re
import sys


class Vol:
    def __init__(self, pilote, date, vtype, deco, aterro):
        self.pilote = pilote
        self.vtype = vtype
        self.deco = deco
        self.aterro = aterro
        self.date = date
        self.link = None
        self.balises = None

    def __repr__(self):
        s = """Vol de {0}, le {1}.
 - deco: {2} / aterro: {3}
 - balises: {4}
 - type: {5}
 - link: {6}
""".format(self.pilote, self.date, self.deco, self.aterro, self.balises, self.vtype, self.link)
        return s

balises_re=re.compile('href="(?P<gpshref>.*)">gps.*balises : (?P<balises>.*)</font></i></td>')
info_vol_re=re.compile('tous les vols du (?P<date>[^"]*)">.*</a></td><td><a href="(?=/pilote)(?P<pilotehref>[^"]*)">(?P<pilote>[^<]*)</a>.*type">(?P<type>[^<]*).*<td>(?P<deco>.*)</td><td>(?P<aterro>.*)</td><td alig')

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
                   m.group('aterro'))
        continue
    
    m = balises_re.search(l)
    if m:
        cvol.link = m.group('gpshref')
        cvol.balises = m.group('balises')
        all_vols.append(cvol)
        cvol = None

print all_vols


    
