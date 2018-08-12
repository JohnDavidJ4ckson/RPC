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
import CMS_lumi, tdrstyle

def main():
  lines = []
  with open('DTrates2018.txt', 'rw') as shakes:
    for line in shakes:
      l = re.compile("( *)").split(line.rstrip())
      lines.append(l)
#  print lines
  name = []
  rate = []
  wheel = []
  station = []
  section = []
  i = 1
  numberMatch = re.compile("(\D\D|\D\D\D)(-?\d*)$")
  for line in lines:
#########################
# Testing prints
#########################
    rateStrings = line[-1]
    rateWheel   = line[0].split("/")[0]
    rateStation = line[0].split("/")[2]
    rateSection = line[0].split("/")[1]
    print i, rateStrings, rateWheel, rateStation, rateSection
    i += 1
#########################
    wheelSplit   = numberMatch.match(rateWheel)
    stationSplit = numberMatch.match(rateStation)
    sectionSplit = numberMatch.match(rateSection)

    rateValue     = float(line[-1])
    wheelValue   = float(wheelSplit.group(2))
    statiValue   = float(stationSplit.group(2))
    sectionValue = float(sectionSplit.group(2))

    rate.append(rateValue)
    wheel.append(wheelValue)  
    station.append(statiValue)
    section.append(sectionValue)

  print rate
  print wheel
  print station
  print section

if __name__ == "__main__":
  main()

