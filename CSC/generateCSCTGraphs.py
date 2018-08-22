#!/usr/bin/env python
import re
from ROOT import *
from array import array
#from numpy import median
#import numpy as np
#from scipy import stats
import read2018Neg
import read2018Pos

## Null -> List
## This function gathers the info of both eta and rates 
## then summs it up into a list of dictionaries
def the_list(etaInfo):
  eta = [ -x for x in etaInfo] + etaInfo
  ratesNeg, keysNeg = read2018Neg.main()
  ratesPos, keysPos = read2018Pos.main()
  rates = ratesNeg + ratesPos
  keys = keysNeg + keysPos
  theList = [ keys, eta, rates]
  #print theList
  return theList

## array, array, string -> TGraph
## The function recieves an x and y values to create
## a tgraph of them with the given name.
## This function is imported for use in the etaDistro.py file
def create_tgraphs(x, y, name):
  #print "------ Creating Wheel TGraph ----------"
  n = len(x)
  gr = TGraph(n,x,y)
  gr.SetMarkerColor( kRed+3 )
  gr.SetMarkerStyle( 20 )
  gr.SetMarkerSize( 1.5 )
  gr.SetLineColor( 5 )
  gr.SetLineWidth( 7 )
  gr.SetTitle( name )
  gr.GetXaxis().SetTitle( '#eta' )
  gr.GetYaxis().SetTitle( 'CSC single hit rate (Hz/cm^{2})' )
  return gr

def main():
  stations = ['ME1', 'ME2', 'ME3', 'ME4']
  etaList = [1.9, 1.4, 1.0, 2.0, 1.3, 2.1, 1.4, 2.1, 1.5] # eta positions "by eye"
  a = the_list(etaList)
  xME1, xME2, xME3, xME4 = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )
  yME1, yME2, yME3, yME4 = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )

  indexME1 = [0, 1, 2, 9, 10, 11]
  indexME2 = [3, 4, 12, 13]
  indexME3 = [5, 6, 14, 15]
  indexME4 = [7, 8, 16, 17]

  grList = []
  xlist = [xME1, xME2, xME3, xME4]
  ylist = [yME1, yME2, yME3, yME4]

  for i in range(len(a[1])):
    #print i
    if i in indexME1: 
      xlist[0].append(a[1][i])
      ylist[0].append(a[2][i])
    if i in indexME2: 
      xlist[1].append(a[1][i]) 
      ylist[1].append(a[2][i])
    if i in indexME3: 
      xlist[2].append(a[1][i]) 
      ylist[2].append(a[2][i])
    if i in indexME4: 
      xlist[3].append(a[1][i]) 
      ylist[3].append(a[2][i])

  for s in stations:
    grList.append(create_tgraphs(xlist[stations.index(s)], ylist[stations.index(s)], s))
  #print grList
  return grList

if __name__ == "__main__":
  main()

