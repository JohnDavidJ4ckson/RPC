#!/usr/bin/env python
import re
import json
import sys
import getopt
from ROOT import *
from ROOT import gPad
from ROOT import TCanvas, TGraph
from ROOT import gROOT
from array import array
from numpy import median
import numpy as np
from scipy import stats
import ROOT as rt

def main():
  lines = []
  with open('CSC_background_at_48_2017_2018.txt', 'rw') as shakes:
    for line in shakes:
      lines.append(line.rstrip())
  print len(lines)

#  name = []
  rate = []
#  wheel = []
  station = []
  chamber = []
  chamberTest = []
  year = []
  dic = {}
  i = 1
#  numberMatch = re.compile("(\D\D|\D\D\D)(-?\d*)$")
  for line in lines:
    print i#lines.index(line)+1
    l = re.compile("\s+").split(line.rstrip()) 

    if i in range(5,41):
      if len(l) == 11:
        chamberTest.append(int(l[-10]))
        print 'fill shit'
      if len(l) == 8:
        chamberTest.append(int(l[-7]))
        print 'shit filled'

    if i in range(47,83):
      if len(l) == 11:
        chamberTest.append(int(l[-10]))
        print 'fill shit'
      if len(l) == 8:
        chamberTest.append(int(l[-7]))
        print 'shit filled'

    if i in range(89,125):
      if len(l) == 11:
        chamberTest.append(int(l[-10]))
        print 'fill shit'
      if len(l) == 8:
        chamberTest.append(int(l[-7]))
        print 'shit filled'

    if i in range(131,167):
      if len(l) == 11:
        chamberTest.append(int(l[-10]))
        print 'fill shit'
      if len(l) == 8:
        chamberTest.append(int(l[-7]))
        print 'shit filled'
    i += 1

  print chamber
  print chamberTest
##########################
## Testing prints
##########################
#    rateStrings = line[-1]
#    rateWheel   = line[0].split("/")[0]
#    rateStation = line[0].split("/")[2]
#    rateSection = line[0].split("/")[1]
#    print i, rateStrings, rateWheel, rateStation, rateSection
#    i += 1
##########################
#    wheelSplit   = numberMatch.match(rateWheel)
#    stationSplit = numberMatch.match(rateStation)
#    sectionSplit = numberMatch.match(rateSection)
#
#    rateValue     = int(line[-1])
#    wheelValue   = int(wheelSplit.group(2))
#    statiValue   = int(stationSplit.group(2))
#    sectionValue = int(sectionSplit.group(2))
#
#    rate.append(rateValue)
#    wheel.append(wheelValue)  
#    station.append(statiValue)
#    section.append(sectionValue)
#
#  print rate
#  print wheel
#  print station
#  print section

if __name__ == "__main__":
  main()

