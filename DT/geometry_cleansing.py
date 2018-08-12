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
  with open('Geometry.out', 'rw') as shakes:
    for line in shakes:
      l = re.compile("( *)").split(line)
      lines.append(l)
#  print lines
  name = []
  eta = []
  wheel = []
  station = []
  section = []
  i = 1
  for line in lines:
#########################
# Testing prints should be commented when running
#########################
    etaStrings = line[-3]
    etaWheel   = line[0]
    etaStation = line[2]
    etaSection = line[4]
#    print i, etaStrings, etaWheel, etaStation, etaSection
    i += 1
#########################
    etaValue     = float(line[-3].split("=")[-1])
    wheelValue   = float(line[0].split(":")[-1])
    stationValue = float(line[2].split(":")[-1])
    sectionValue = float(line[4].split(":")[-1])
#    print etaValue, wheelValue, stationValue, sectionValue
    eta.append(etaValue)
    wheel.append(wheelValue)
    station.append(stationValue)
    section.append(sectionValue)
    name.append(etaWheel+" "+etaStation+" "+etaSection)
  print eta
  print wheel
  print station
  print section
#  print name

if __name__ == "__main__":
  main()


