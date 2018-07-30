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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def etaWheel_lists():
  lines = []
  with open('WGeometry.out', 'rw') as shakes:
    for line in shakes:
      y = line.split(" glob(X,Y,Z)")
      lines.append(y)
  name = []
  etaMin = []
  etaMax = []
  etaAvg = []
  vMin = []
  vMax = []
  for line in lines:
    nameList = line[0]
    name.append(nameList.rstrip())
    # Informacion del first strip
    minEtaList0 = line[1].split("(")
    minEtaList1 = minEtaList0[1].split(",")   # Las entradas 0 y 1 son las coordenadas X y Y del strip
    minEtaList2 = minEtaList1[2].split(r")")  # La entrada 0 de esta lista es la coordenada Z del strip
    minX = float(minEtaList1[0])
    minY = float(minEtaList1[1])
    minZ = float(minEtaList2[0])
    v1 = TVector3(minX,minY,minZ)
    vMin.append(v1)
    eta1 = v1.Eta()
    etaMin.append(eta1)
    # Informacion del last strip
    maxEtaList0 = line[2].split("(")
    maxEtaList1 = maxEtaList0[1].split(",")   # Las entradas 0 y 1 son las coordenadas X y Y del strip
    maxEtaList2 = maxEtaList1[2].split(r")")  # La entrada 0 de esta lista es la coordenada Z del strip
    maxX = float(maxEtaList1[0])
    maxY = float(maxEtaList1[1])
    maxZ = float(maxEtaList2[0])
    v2 = TVector3(minX,minY,minZ)
    vMax.append(v2)
    eta2 = v2.Eta()
    etaMax.append(eta2)
    avgEtaValue = ( eta1 + eta2 ) /2
    etaAvg.append(avgEtaValue)

  List = [name, etaAvg]
  return List


def main():
  temp = etaWheel_lists()
  print type(temp[0])
  print len(temp[0])
  name = temp[0]
  eta = temp[1]
  print type(temp[1])
  print len(temp[1])

  with open('dataW+0.json', 'w') as outfile:
    #json.dump(eta, outfile)
    for i in range(len(name)):
      outfile.write( str(name[i]) +" "+ str(eta[i])+"\n" )




if __name__ == "__main__":
  calling = main()
