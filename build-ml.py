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

import csv
import sys

selectors = ['Bureau', 'Grimpe', 'Parapentiste', 'Compétiteur parapente']

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

if options.selection == None :
    print "I don't know what to select... (--select)"
    sys.exit(-1)

if options.selection not in selectors:
    print "'" + options.selection + "' not a valid selector. Valid are : " + ", ".join(selectors)
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
