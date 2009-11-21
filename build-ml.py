#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser

import csv
import sys

selectors = [u'Bureau', u'Grimpe', u'Parapentiste', u'Compétiteur parapente']

parser = OptionParser()

parser.add_option("-f", "--file", dest="filename",
                  help="CSV file FILE", metavar="FILE")

parser.add_option("-s", "--select", dest="selection",
                  help="Column used for selection in " + str(selectors),
                  metavar="SELECT")

(options, args) = parser.parse_args()

if options.filename == None:
    print "Missing CSV file (--file)..."
    sys.exit(-1)

if options.selection == None:
    print "I don't know what to select... (--select)"
    sys.exit(-1)

file = csv.reader(open(options.filename,"r"), delimiter=',')

col_filter = options.selection

start = True
mail_idx = None
filter_idx = None

result = {}

for row in file:
    if start:
        mail_idx = row.index('E-mail')
        filter_idx = row.index(col_filter)
        start = False
        continue

    if row[filter_idx] == '1':
        result[row[mail_idx].strip()] = 1

print "\n".join(result.keys())
