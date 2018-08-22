#!/usr/bin/env python
import math
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
from numpy import isnan
#import numpy as np
#from scipy import stats
import ROOT as rt
import CMS_lumi, tdrstyle
import generateDTTGraphs
import generateCSCTGraphs

## Value -> Boolean
## This function returns True if the given object is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

## Null -> List of lists [string, double]
## The function uses a fixed json file to return a list of lists with 
## RPC Id names in the first entry and the corresponding rates in 
## the second entry. The IDnames are createad as they would correspond
## to RPC in the Endcap section.
def ratesEndcap_list():
  runNumfile = "ratesAt1p5.json" #"output_rolls2018.json"
  with open(runNumfile) as dataf:
    rates1 = json.loads(dataf.read())
  rolls = ["_A","_B","_C"] #, "_D"]
  chambers = [
             "01","02","03","04","05","06","07","08","09",
        "10","11","12","13","14","15","16","17","18","19",
        "20","21","22","23","24","25","26","27","28","29",
        "30","31","32","33","34","35","36"
        ]
  ring = ["_R2", "_R3"]
  names = []
  rates = []
  for r in ring:
    for roll in rolls:
      #rates = []
      for c in chambers:
        try:
          #print r
          if float(rates1[endcapSection+r+"_CH"+c+roll]) == 0: continue
          rates.append(float(rates1[endcapSection+r+"_CH"+c+roll]))
          names.append(endcapSection+r+"_CH"+c+roll)
        except KeyError:
          continue
  #print sorted(names)
  return [names, rates]

## Null -> List of lists [string, double]
## The function uses a fixed json file to return a list of lists with 
## RPC Id names in the first entry and the corresponding rates in 
## the second entry. The IDnames are createad as they would correspond
## to RPC in the Barrel section.
def ratesWheel_lists():
  runNumfile = "ratesAt1p5.json" #"output_rolls2018.json"
  with open(runNumfile) as dataf:
    rates1 = json.loads(dataf.read())
  wheels = ["0", "1", "2"]
  rolls = ["1", "2", "3", "4"]
  subrolls = ["","+","-","in","out"]#, "++", "--"]
  chambers = [
             "01","02","03","05","06",
             "07","08","10","12"] # faltan 4, 9, 11
  ring = ["Forward", "Middle", "Backward"]
  parameters = ["W"+wheelSection0+w+"_"+wheelSection+s+"_S"+c+"_"+ri for w in wheels
                for s in subrolls for c in chambers for ri in ring ]
                #if ( (w == "0") and (ri == "Forward") ) or ( w!="0" )]
  #W+2_RB2out_S10_Middle
  names = []
  rates = []
  for p in parameters:
    try:
      if float(rates1[p]) == 0: continue
      rates.append(float(rates1[p]))
      names.append(p)
    except KeyError:
      continue
  return [names, rates]

## Null ->  List of lists [string, double]
## The function uses a fixed txt file with the geometric information
## of the RPC's in the barrel and returns a list of names and their
## corresponding pseudorapidity mean location.
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

## Null ->  List of lists [string, double]
## The function uses a fixed txt file with the geometric information
## of the RPC's in the endcaps and returns a list of names and their
## corresponding pseudorapidity mean location.
def etaEndcap_list():
  lines = []
  with open('file.out', 'rw') as shakes:
    for line in shakes:
      y = line.split(",")
      lines.append(y)
  name = []
  etaMin = []
  etaMax = []
  etaAvg = []
  for line in lines:
    nameList = line[0]
    name.append(nameList.rstrip())
    minEtaList = line[3].split(" ")
    minEtaValue = [ x for x in minEtaList if is_number(x) ]
    etaMin.append(float(minEtaValue[0]))
    maxEtaList = line[4].split(" ")
    maxEtaValue = [ x for x in maxEtaList if is_number(x) ]
    etaMax.append(float(maxEtaValue[0]))
    avgEtaValue = (float(minEtaValue[0]) + float(maxEtaValue[0]) ) /2
    etaAvg.append(float(avgEtaValue))
  List = [name, etaAvg]
  return List

## List of lists [string, double], 
## List of lists [string, double]  -> Dictionary
## The function maps the rates and pseudorapidities that share ID 
## names to each other and returns them in a dictionary
def intersect_list(etaList, ratesList):
  intersect = set(etaList[0]).intersection(ratesList[0])
  dict0 = {}
  for i in intersect:
    etaIndex = etaList[0].index(i)
    rateIndex = ratesList[0].index(i)
    indict = { "eta": etaList[1][etaIndex],
               "rates":ratesList[1][rateIndex] }
    dict0[i] = indict
  return dict0

## (0 or 1), Dictionary,
## array, array, -> Null
## The function fills the given X and Y arrays with the median 
## (or average) over the chambers in the RPC subdivions of interest
def average_chambers(wheel, dictionary, X, Y):
  if wheel == 1:
    wheels = ["0", "1", "2"]
    rolls = ["1", "2", "3", "4"]
    subrolls = ["","+","-","in","out"]#, "++", "--"]
    chambers = [
               "01","02","03","04","05","06",
               "07","08","09","10","11","12"] #faltan 9, 11 y 4
    ring = ["Forward", "Middle", "Backward"]
    for w in wheels:
      #if wheelSection == "RB3" or wheelSection == "RB4":
      for s in subrolls:
        for ri in ring:
          #for c in chambers:
          eta = [float( v["eta"] ) for k, v in dictionary.items() for c in chambers if not isnan(v["eta"])
               if k == "W"+wheelSection0+w+"_"+wheelSection+s+"_S"+c+"_"+ri]
          rates = [float( v["rates"] ) for k, v in dictionary.items() for c in chambers if not isnan(v["rates"])
                 if k == "W"+wheelSection0+w+"_"+wheelSection+s+"_S"+c+"_"+ri]
          names = [k for k, v in dictionary.items()
                 for c in chambers if k == "W"+wheelSection0+w+"_"+wheelSection+s+"_S"+c+"_"+ri]
          if rates:
            #print names
            #print eta
            #print median(eta)
            X.append( median(eta)   )  #sum(eta)/len(eta) )
            Y.append( median(rates) )  #sum(rates)/len(rates) ) 
            #print rates
            #print median(rates)
      #elif wheelSection == "RB1" or wheelSection == "RB2":
      #  for ri in ring:
      #    eta = [v["eta"] for k, v in dictionary.items() for s in subrolls
      #           for c in chambers if k == "W"+wheelSection0+w+"_"+wheelSection+s+"_S"+c+"_"+ri]
      #    rates = [v["rates"] for k, v in dictionary.items() for s in subrolls
      #           for c in chambers if k == "W"+wheelSection0+w+"_"+wheelSection+s+"_S"+c+"_"+ri]
      #    names = [k for k, v in dictionary.items() for s in subrolls
      #           for c in chambers if k == "W"+wheelSection0+w+"_"+wheelSection+s+"_S"+c+"_"+ri]
      #    if rates:# and len(rates) != 1: 
      #      print names
      #      X.append( median(eta)   )  #sum(eta)/len(eta) )
      #      Y.append( median(rates) )  #sum(rates)/len(rates) )

  elif wheel == 0:
    rolls = ["_A","_B","_C"] #, "_D"]
    chambers = [
               "01","02","03","04","05","06","07","08","09",
          "10","11","12","13","14","15","16","17","18","19",
          "20","21","22","23","24","25","26","27","28","29",
          "30","31","32","33","34","35","36"
          ]
    ring = ["_R2", "_R3"]
    for r in ring:
      for roll in rolls:
        eta = [float( v["eta"] ) for k, v in dictionary.items() for c in chambers if k == endcapSection+r+"_CH"+c+roll if not isnan(v["eta"])]
        rates = [float( v["rates"] ) for k, v in dictionary.items() for c in chambers if k == endcapSection+r+"_CH"+c+roll if not isnan( v["rates"])]
        if rates:# and len(rates) != 1:
          #X.append( max(set(eta), key=eta.count)     )
          #Y.append( max(set(rates), key=rates.count) )
          X.append( median(eta) ) #sum(eta)/len(eta) ) 
          Y.append( median(rates) )  #sum(rates)/len(rates) )

## Null -> array, array, array, array
## The main function calls the creation of eta and rates lists
## then maps them to each othar and takes the chamber median
## (or average) to a set of four arrays that get returned.
## Nomenclature: x - Eta
##               y - Rates
##               W - wheel
##               E - endcap
def main():
  wheelEtaList = etaWheel_lists() #[names, eta] 
  endcapEtaList = etaEndcap_list() #[names, eta] 
  wheelRatesList = ratesWheel_lists() #[names, rates]
  endcapRatesList = ratesEndcap_list() #[names, rates]
  wheelIntersect = intersect_list(wheelEtaList,wheelRatesList) #name{eta, rates}
  endcapIntersect = intersect_list(endcapEtaList,endcapRatesList) #name{eta, rates}
  xW, yW = array( 'd' ), array( 'd' )
  xE, yE = array( 'd' ), array( 'd' )
  average_chambers(1, wheelIntersect,  xW, yW)
  average_chambers(0, endcapIntersect, xE, yE)
  return xW, yW, xE, yE

## 48 arrays -> Null
## This function recieves 14 arrays for eta wheel, eta endcaps, 
## rates wheel and rates endcap. The function creates 3 canvas.
## On the first canvas 5 rate vs eta plots are presented for
## sections RB1in, RB1out, RB2, RB3, and RB4 in the barrel and
## RE1 (twice), RE2, RE3, and RE4 in the endcaps.
## The second and third canvas's are comparisons between the inner
## and outer parts of RB1 and RB2 respectively.
## The canvas are saved to .gif and .png
def eta_plot(X0W,Y0W,X1W,Y1W,X2W,Y2W,X3W, Y3W, X4W, Y4W, X5W, Y5W, X6W, Y6W,
             X7W,Y7W,X8W,Y8W,X9W,Y9W,X10W,Y10W,X11W,Y11W,X12W,Y12W,X13W,Y13W,
             X0E,Y0E,X1E,Y1E,X2E,Y2E,X3E, Y3E, X4E, Y4E, X5E, Y5E, X6E, Y6E,
             X7E,Y7E,X8E,Y8E,X9E,Y9E,X10E,Y10E,X11E,Y11E,X12E,Y12E,X13E,Y13E):
  print "------ Setting Up Format ----------"
  tdrstyle.setTDRStyle()
  #change the CMS_lumi variables (see CMS_lumi.py)
  CMS_lumi.writeExtraText = 1
  CMS_lumi.extraText  = "Preliminary"
  CMS_lumi.extraText2 = "2018 pp data"
  CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
  CMS_lumi.writeTitle = 1
  CMS_lumi.textTitle = 'title'

  iPos = 11
  if( iPos==0 ): CMS_lumi.relPosX = 0.12

  H_ref = 600;
  W_ref = 800;
  W = W_ref  
  H = H_ref
  iPeriod = 0
  # references for T, B, L, R  
  T = 0.08*H_ref
  B = 0.12*H_ref
  L = 0.12*W_ref
  R = 0.04*W_ref

  
  print "------ Creating Wheel TGraph ----------"
  n0W = len(X0W)
  gr0W = TGraph(n0W,X0W,Y0W)
  gr0W.SetMarkerColor( kRed )
  gr0W.SetMarkerStyle( 20 )
  gr0W.SetMarkerSize( 1.5 )
  gr0W.SetTitle( 'RB1 in' )
  gr0W.GetXaxis().SetTitle( '#eta' )
  gr0W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n1W = len(X1W)
  gr1W = TGraph(n1W,X1W,Y1W)
  gr1W.SetLineColor( 2 )
  gr1W.SetLineWidth( 4 )
  gr1W.SetMarkerColor( kBlue )
  gr1W.SetMarkerStyle( 29 )
  gr1W.SetMarkerSize( 1.7 )
  gr1W.SetTitle( 'Layer 1 Wheel' )
  gr1W.GetXaxis().SetTitle( '#eta' )
  gr1W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n2W = len(X2W)
  gr2W = TGraph(n2W,X2W,Y2W)
  gr2W.SetLineColor( 3 )
  gr2W.SetLineWidth( 5 )
  gr2W.SetMarkerColor( kRed+2 )
  gr2W.SetMarkerStyle( 21 )
  gr2W.SetMarkerSize( 1.5 )
  gr2W.SetTitle( 'Layer 2 Wheel') 
  gr2W.GetXaxis().SetTitle( '#eta' )
  gr2W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n3W = len(X3W)
  gr3W = TGraph(n3W,X3W,Y3W)
  gr3W.SetLineColor( 4 )
  gr3W.SetLineWidth( 6 )
  gr3W.SetMarkerColor( kRed )
  gr3W.SetMarkerStyle( 21 )
  gr3W.SetMarkerSize( 1.5 )
  gr3W.SetTitle( 'Layer 3 Wheel' )
  gr3W.GetXaxis().SetTitle( '#eta' )
  gr3W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n4W = len(X4W)
  gr4W = TGraph(n4W,X4W,Y4W)
  gr4W.SetLineColor( 5 )
  gr4W.SetLineWidth( 7 )
  gr4W.SetMarkerColor( kBlue )
  gr4W.SetMarkerStyle( 23 )
  gr4W.SetMarkerSize( 1.5 )
  gr4W.SetTitle( 'Layer 4 Wheel' )
  gr4W.GetXaxis().SetTitle( '#eta' )
  gr4W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  print "------ Creating Endcap TGraph ----------"
  n0E = len(X0E)
  gr0E = TGraph(n0E,X0E,Y0E)
  gr0E.SetLineColor( 2 )
  gr0E.SetLineWidth( 4 )
  gr0E.SetMarkerColor( kRed )
  gr0E.SetMarkerStyle( 24 )
  gr0E.SetMarkerSize( 1.5 )
  gr0E.SetTitle( 'Layer 1 Endcap' )
  gr0E.GetXaxis().SetTitle( '#eta' )
  gr0E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n1E = len(X1E)
  gr1E = TGraph(n1E,X1E,Y1E)
  gr1E.SetLineColor( 2 )
  gr1E.SetLineWidth( 4 )
  gr1E.SetMarkerColor( kBlue )
  gr1E.SetMarkerStyle( 30 )
  gr1E.SetMarkerSize( 1.5 )
  gr1E.SetTitle( 'Layer 1 Endcap' )
  gr1E.GetXaxis().SetTitle( '#eta' )
  gr1E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n2E = len(X2E)
  gr2E = TGraph(n2E,X2E,Y2E)
  gr2E.SetLineColor( 3 )
  gr2E.SetLineWidth( 5 )
  gr2E.SetMarkerColor( kRed+2 )
  gr2E.SetMarkerStyle( 25 )
  gr2E.SetMarkerSize( 1.5 )
  gr2E.SetTitle( 'Layer 2 Endcap')
  gr2E.GetXaxis().SetTitle( '#eta' )
  gr2E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n3E = len(X3E)
  gr3E = TGraph(n3E,X3E,Y3E)
  gr3E.SetLineColor( 4 )
  gr3E.SetLineWidth( 6 )
  gr3E.SetMarkerColor( kRed )
  gr3E.SetMarkerStyle( 25 )
  gr3E.SetMarkerSize( 1.5 )
  gr3E.SetTitle( 'Layer 3 Endcap' )
  gr3E.GetXaxis().SetTitle( '#eta' )
  gr3E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n4E = len(X4E)
  gr4E = TGraph(n4E,X4E,Y4E)
  gr4E.SetLineColor( 5 )
  gr4E.SetLineWidth( 7 )
  gr4E.SetMarkerColor( kBlue )
  gr4E.SetMarkerStyle( 32 )
  gr4E.SetMarkerSize( 1.5 )
  gr4E.SetTitle( 'Layer 4 Endcap' )
  gr4E.GetXaxis().SetTitle( '#eta' )
  gr4E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  print "------ Creating Wheel TGraph ----------"
  n5W = len(X5W)
  gr5W = TGraph(n5W,X5W,Y5W)
  gr5W.SetLineColor( 2 )
  gr5W.SetLineWidth( 4 )
  gr5W.SetMarkerColor( 6 )
  gr5W.SetMarkerStyle( 22 )
  gr5W.SetMarkerSize( 1.5 )
  gr5W.SetTitle( 'Layer 1 Wheel' )
  gr5W.GetXaxis().SetTitle( '#eta' )
  gr5W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n6W = len(X6W)
  gr6W = TGraph(n6W,X6W,Y6W)
  gr6W.SetLineColor( 3 )
  gr6W.SetLineWidth( 5 )
  gr6W.SetMarkerColor( 28 )
  gr6W.SetMarkerStyle( 23 )
  gr6W.SetMarkerSize( 1.7 )
  gr6W.SetTitle( 'Layer 2 Wheel')
  gr6W.GetXaxis().SetTitle( '#eta' )
  gr6W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n7W = len(X7W)
  gr7W = TGraph(n7W,X7W,Y7W)
  gr7W.SetLineColor( 4 )
  gr7W.SetLineWidth( 6 )
  gr7W.SetMarkerColor( kRed )
  gr7W.SetMarkerStyle( 20 )
  gr7W.SetMarkerSize( 1.5 )
  gr7W.SetTitle( 'Layer 3 Wheel' )
  gr7W.GetXaxis().SetTitle( '#eta' )
  gr7W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n8W = len(X8W)
  gr8W = TGraph(n8W,X8W,Y8W)
  gr8W.SetLineColor( 5 )
  gr8W.SetLineWidth( 7 )
  gr8W.SetMarkerColor( kBlue )
  gr8W.SetMarkerStyle( 29 )
  gr8W.SetMarkerSize( 1.5 )
  gr8W.SetTitle( 'Layer 4 Wheel' )
  gr8W.GetXaxis().SetTitle( '#eta' )
  gr8W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n9W = len(X9W)
  gr9W = TGraph(n9W,X9W,Y9W)
  gr9W.SetLineColor( 5 )
  gr9W.SetLineWidth( 7 )
  gr9W.SetMarkerColor( kRed+2 )
  gr9W.SetMarkerStyle( 21 )
  gr9W.SetMarkerSize( 1.5 )
  gr9W.SetTitle( 'Layer 4 Wheel' )
  gr9W.GetXaxis().SetTitle( '#eta' )
  gr9W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n10W = len(X10W)
  gr10W = TGraph(n10W,X10W,Y10W)
  gr10W.SetLineColor( 5 )
  gr10W.SetLineWidth( 7 )
  gr10W.SetMarkerColor( kRed )
  gr10W.SetMarkerStyle( 21 )
  gr10W.SetMarkerSize( 1.5 )
  gr10W.SetTitle( 'Layer 4 Wheel' )
  gr10W.GetXaxis().SetTitle( '#eta' )
  gr10W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n11W = len(X11W)
  gr11W = TGraph(n11W,X11W,Y11W)
  gr11W.SetLineColor( 5 )
  gr11W.SetLineWidth( 7 )
  gr11W.SetMarkerColor( kBlue )
  gr11W.SetMarkerStyle( 23 )
  gr11W.SetMarkerSize( 1.5 )
  gr11W.SetTitle( 'Layer 4 Wheel' )
  gr11W.GetXaxis().SetTitle( '#eta' )
  gr11W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n12W = len(X12W)
  gr12W = TGraph(n12W,X12W,Y12W)
  gr12W.SetLineColor( 5 )
  gr12W.SetLineWidth( 7 )
  gr12W.SetMarkerColor( 6 )
  gr12W.SetMarkerStyle( 22 )
  gr12W.SetMarkerSize( 1.5 )
  gr12W.SetTitle( 'Layer 4 Wheel' )
  gr12W.GetXaxis().SetTitle( '#eta' )
  gr12W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n13W = len(X13W)
  gr13W = TGraph(n13W,X13W,Y13W)
  gr13W.SetLineColor( 5 )
  gr13W.SetLineWidth( 7 )
  gr13W.SetMarkerColor( 28 )
  gr13W.SetMarkerStyle( 23 )
  gr13W.SetMarkerSize( 1.5 )
  gr13W.SetTitle( 'Layer 4 Wheel' )
  gr13W.GetXaxis().SetTitle( '#eta' )
  gr13W.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )


  print "------ Creating Endcap TGraph ----------"
  n5E = len(X5E)
  gr5E = TGraph(n5E,X5E,Y5E)
  gr5E.SetLineColor( 2 )
  gr5E.SetLineWidth( 4 )
  gr5E.SetMarkerColor( 6 )
  gr5E.SetMarkerStyle( 26 )
  gr5E.SetMarkerSize( 1.5 )
  gr5E.SetTitle( 'Layer 1 Endcap' )
  gr5E.GetXaxis().SetTitle( '#eta' )
  gr5E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n6E = len(X6E)
  gr6E = TGraph(n6E,X6E,Y6E)
  gr6E.SetLineColor( 3 )
  gr6E.SetLineWidth( 5 )
  gr6E.SetMarkerColor( 28 )
  gr6E.SetMarkerStyle( 32 )
  gr6E.SetMarkerSize( 1.5 )
  gr6E.SetTitle( 'Layer 2 Endcap')
  gr6E.GetXaxis().SetTitle( '#eta' )
  gr6E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n7E = len(X7E)
  gr7E = TGraph(n7E,X7E,Y7E)
  gr7E.SetLineColor( 4 )
  gr7E.SetLineWidth( 6 )
  gr7E.SetMarkerColor( kRed )
  gr7E.SetMarkerStyle( 24 )
  gr7E.SetMarkerSize( 1.5 )
  gr7E.SetTitle( 'Layer 3 Endcap' )
  gr7E.GetXaxis().SetTitle( '#eta' )
  gr7E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n8E = len(X8E)
  gr8E = TGraph(n8E,X8E,Y8E)
  gr8E.SetLineColor( 5 )
  gr8E.SetLineWidth( 7 )
  gr8E.SetMarkerColor( kBlue )
  gr8E.SetMarkerStyle( 30 )
  gr8E.SetMarkerSize( 1.5 )
  gr8E.SetTitle( 'Layer 4 Endcap' )
  gr8E.GetXaxis().SetTitle( '#eta' )
  gr8E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n9E = len(X9E)
  gr9E = TGraph(n9E,X9E,Y9E)
  gr9E.SetLineColor( 5 )
  gr9E.SetLineWidth( 7 )
  gr9E.SetMarkerColor( kRed+2 )
  gr9E.SetMarkerStyle( 25 )
  gr9E.SetMarkerSize( 1.5 )
  gr9E.SetTitle( 'Layer 4 Endcap' )
  gr9E.GetXaxis().SetTitle( '#eta' )
  gr9E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n10E = len(X10E)
  gr10E = TGraph(n10E,X10E,Y10E)
  gr10E.SetLineColor( 5 )
  gr10E.SetLineWidth( 7 )
  gr10E.SetMarkerColor( kRed )
  gr10E.SetMarkerStyle( 25 )
  gr10E.SetMarkerSize( 1.5 )
  gr10E.SetTitle( 'Layer 4 Endcap' )
  gr10E.GetXaxis().SetTitle( '#eta' )
  gr10E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n11E = len(X11E)
  gr11E = TGraph(n11E,X11E,Y11E)
  gr11E.SetLineColor( 5 )
  gr11E.SetLineWidth( 7 )
  gr11E.SetMarkerColor( kBlue )
  gr11E.SetMarkerStyle( 32 )
  gr11E.SetMarkerSize( 1.5 )
  gr11E.SetTitle( 'Layer 4 Endcap' )
  gr11E.GetXaxis().SetTitle( '#eta' )
  gr11E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n12E = len(X12E)
  gr12E = TGraph(n12E,X12E,Y12E)
  gr12E.SetLineColor( 5 )
  gr12E.SetLineWidth( 7 )
  gr12E.SetMarkerColor( 6 )
  gr12E.SetMarkerStyle( 26 )
  gr12E.SetMarkerSize( 1.5 )
  gr12E.SetTitle( 'Layer 4 Endcap' )
  gr12E.GetXaxis().SetTitle( '#eta' )
  gr12E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  n13E = len(X13E)
  gr13E = TGraph(n13E,X13E,Y13E)
  gr13E.SetLineColor( 5 )
  gr13E.SetLineWidth( 7 )
  gr13E.SetMarkerColor( 28 )
  gr13E.SetMarkerStyle( 32 )
  gr13E.SetMarkerSize( 1.5 )
  gr13E.SetTitle( 'Layer 4 Endcap' )
  gr13E.GetXaxis().SetTitle( '#eta' )
  gr13E.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  print "----- Creating TCanvas -----"
  H = 800
  W = 1600
  canv = TCanvas("canv", "Canvas",50,50,W,H)
  canv.SetFillColor(0)
  canv.SetBorderMode(0)
  canv.SetFrameFillStyle(0)
  canv.SetFrameBorderMode(0)
  canv.SetLeftMargin( L/W )
  canv.SetRightMargin( R/W )
  canv.SetTopMargin( T/H )
  canv.SetBottomMargin( B/H )
  canv.SetTickx(0)
  canv.SetTicky(0)
  canv.Divide(3,2,0.001,0.001)
  CMS_lumi.CMS_lumi(canv, iPeriod, iPos)
  canv.cd()
  canv.Update()
  maxY = 1000

  canv.cd(1)
  gPad.SetLogy()
  print " ------------ Creating TMultiGraph -----------"
  mg1 = TMultiGraph()
  #graphAxis(mg1)
  mg1.Add(gr0E,"AP")
  mg1.Add(gr0W,"AP")
  mg1.Add(gr7E,"AP")
  mg1.Add(gr7W,"AP")
  mg1.Draw("a")
  mg1.SetTitle( 'RB1in')
  mg1.GetXaxis().SetTitle( '#eta' )
  mg1.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mg1.SetMaximum(maxY)
  mg1.GetXaxis().SetLabelFont(42)
  mg1.GetXaxis().SetLabelOffset(0.007)
  mg1.GetXaxis().SetLabelSize(0.043)
  mg1.GetXaxis().SetTitleSize(0.05)
  mg1.GetXaxis().SetTitleOffset(1.06)
  mg1.GetXaxis().SetTitleFont(42)
  mg1.GetYaxis().SetLabelFont(42)
  mg1.GetYaxis().SetLabelOffset(0.008)
  mg1.GetYaxis().SetLabelSize(0.05)
  mg1.GetYaxis().SetTitleSize(0.06)
  mg1.GetYaxis().SetTitleOffset(0.87)
  mg1.GetYaxis().SetTitleFont(42)

  pvtxt = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pvtxt.AddText('CMS Preliminary')
  pvtxt.SetFillStyle(0)
  pvtxt.SetBorderSize(0)
  pvtxt.SetTextSize(0.03)
  pvtxt.Draw()
  pvtxt100 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pvtxt100.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pvtxt100.SetFillStyle(0)
  pvtxt100.SetBorderSize(0)
  pvtxt100.SetTextSize(0.03)
  pvtxt100.Draw()

  canv.cd(2)
  gPad.SetLogy()
  gr00 = TGraph()
  gr00.SetMarkerColor( kBlack )
  gr00.SetMarkerStyle( 20 )
  gr00.SetMarkerSize( 1.5 )
  gr01 = TGraph()
  gr01.SetMarkerColor( kBlack )
  gr01.SetMarkerStyle( 24 )
  gr01.SetMarkerSize( 1.5 )

  legend0 = TLegend(0.2, 0.7, .8, .9)
  legend0.SetNColumns(1)
  legend0.AddEntry(gr00, "Barrel", "p")
  legend0.AddEntry(gr01, "Endcaps", "p")
  legend0.Draw("a same")

  legendi = TLegend(0.2, 0.2, .8, .6)
  legendi.SetNColumns(1)
  legendi.AddEntry(gr7W,  "RB1in  + RE1" , "p")
  legendi.AddEntry(gr8W,  "RB1out + RE1" , "p")
  legendi.AddEntry(gr9W,  "RB2 + RE2"    , "p")
#  legendi.AddEntry(gr10W, "RB2in  + RE2" , "p")
#  legendi.AddEntry(gr11W, "RB2out + RE2" , "p")
  legendi.AddEntry(gr12W, "RB3 + RE3"    , "p")
  legendi.AddEntry(gr13W, "RB4 + RE4"    , "p")
  legendi.SetTextSize(0.05)
  legendi.Draw("a");

  canv.cd(3)
  gPad.SetLogy()
  mg2 = TMultiGraph()
  mg2.Add(gr1E,"AP")
  mg2.Add(gr1W,"AP")
  mg2.Add(gr8E,"AP")
  mg2.Add(gr8W,"AP")
  mg2.Draw("a")
  mg2.SetTitle( 'RB1out')
  mg2.GetXaxis().SetTitle( '#eta' )
  mg2.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mg2.SetMaximum(maxY)
  mg2.GetXaxis().SetLabelFont(42)
  mg2.GetXaxis().SetLabelOffset(0.007)
  mg2.GetXaxis().SetLabelSize(0.043)
  mg2.GetXaxis().SetTitleSize(0.05)
  mg2.GetXaxis().SetTitleOffset(1.06)
  mg2.GetXaxis().SetTitleFont(42)
  mg2.GetYaxis().SetLabelFont(42)
  mg2.GetYaxis().SetLabelOffset(0.008)
  mg2.GetYaxis().SetLabelSize(0.05)
  mg2.GetYaxis().SetTitleSize(0.06)
  mg2.GetYaxis().SetTitleOffset(0.87)
  mg2.GetYaxis().SetTitleFont(42)

  pvtxt3 = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pvtxt3.AddText('CMS Preliminary')
  pvtxt3.SetFillStyle(0)
  pvtxt3.SetBorderSize(0)
  pvtxt3.SetTextSize(0.03)
  pvtxt3.Draw()
  pvtxt4 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pvtxt4.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pvtxt4.SetFillStyle(0)
  pvtxt4.SetBorderSize(0)
  pvtxt4.SetTextSize(0.03)
  pvtxt4.Draw()

  canv.cd(4)
  gPad.SetLogy()
  mg3 = TMultiGraph()
  #graphAxis(mg3)
  mg3.Add(gr2E,"AP")
  mg3.Add(gr2W,"AP")
  mg3.Add(gr9E,"AP")
  mg3.Add(gr9W,"AP")
  mg3.Draw("a")
  mg3.SetTitle( 'RB2')
  mg3.GetXaxis().SetTitle( '#eta' )
  mg3.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mg3.SetMaximum(maxY)
  mg3.GetXaxis().SetLabelFont(42)
  mg3.GetXaxis().SetLabelOffset(0.007)
  mg3.GetXaxis().SetLabelSize(0.043)
  mg3.GetXaxis().SetTitleSize(0.05)
  mg3.GetXaxis().SetTitleOffset(1.06)
  mg3.GetXaxis().SetTitleFont(42)
  mg3.GetYaxis().SetLabelFont(42)
  mg3.GetYaxis().SetLabelOffset(0.008)
  mg3.GetYaxis().SetLabelSize(0.05)
  mg3.GetYaxis().SetTitleSize(0.06)
  mg3.GetYaxis().SetTitleOffset(0.87)
  mg3.GetYaxis().SetTitleFont(42)

  pvtxt5 = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pvtxt5.AddText('CMS Preliminary')
  pvtxt5.SetFillStyle(0)
  pvtxt5.SetBorderSize(0)
  pvtxt5.SetTextSize(0.03)
  pvtxt5.Draw()
  pvtxt6 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pvtxt6.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pvtxt6.SetFillStyle(0)
  pvtxt6.SetBorderSize(0)
  pvtxt6.SetTextSize(0.03)
  pvtxt6.Draw()

  canv.cd(5)
  gPad.SetLogy()
  mg4 = TMultiGraph()
  #graphAxis(mg4)
  mg4.Add(gr5E,"AP")
  mg4.Add(gr5W,"AP")
  mg4.Add(gr12E,"AP")
  mg4.Add(gr12W,"AP")
  mg4.Draw("a")
  mg4.SetTitle( 'RB3')
  mg4.GetXaxis().SetTitle( '#eta' )
  mg4.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mg4.SetMaximum(maxY)
  mg4.GetXaxis().SetLabelFont(42)
  mg4.GetXaxis().SetLabelOffset(0.007)
  mg4.GetXaxis().SetLabelSize(0.043)
  mg4.GetXaxis().SetTitleSize(0.05)
  mg4.GetXaxis().SetTitleOffset(1.06)
  mg4.GetXaxis().SetTitleFont(42)
  mg4.GetYaxis().SetLabelFont(42)
  mg4.GetYaxis().SetLabelOffset(0.008)
  mg4.GetYaxis().SetLabelSize(0.05)
  mg4.GetYaxis().SetTitleSize(0.06)
  mg4.GetYaxis().SetTitleOffset(0.87)
  mg4.GetYaxis().SetTitleFont(42)

  pvtxt7 = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pvtxt7.AddText('CMS Preliminary')
  pvtxt7.SetFillStyle(0)
  pvtxt7.SetBorderSize(0)
  pvtxt7.SetTextSize(0.03)
  pvtxt7.Draw()
  pvtxt8 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pvtxt8.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pvtxt8.SetFillStyle(0)
  pvtxt8.SetBorderSize(0)
  pvtxt8.SetTextSize(0.03)
  pvtxt8.Draw()

  canv.cd(6)
  gPad.SetLogy()
  mg5 = TMultiGraph()
  #graphAxis(mg5)
  mg5.Add(gr6E,"AP")
  mg5.Add(gr6W,"AP")
  mg5.Add(gr13E,"AP")
  mg5.Add(gr13W,"AP")
  mg5.Draw("a")
  mg5.SetTitle( 'RB4')
  mg5.GetXaxis().SetTitle( '#eta' )
  mg5.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mg5.SetMaximum(maxY)
  mg5.GetXaxis().SetLabelFont(42)
  mg5.GetXaxis().SetLabelOffset(0.007)
  mg5.GetXaxis().SetLabelSize(0.043)
  mg5.GetXaxis().SetTitleSize(0.05)
  mg5.GetXaxis().SetTitleOffset(1.06)
  mg5.GetXaxis().SetTitleFont(42)
  mg5.GetYaxis().SetLabelFont(42)
  mg5.GetYaxis().SetLabelOffset(0.008)
  mg5.GetYaxis().SetLabelSize(0.05)
  mg5.GetYaxis().SetTitleSize(0.06)
  mg5.GetYaxis().SetTitleOffset(0.87)
  mg5.GetYaxis().SetTitleFont(42)

  pvtxt10 = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pvtxt10.AddText('CMS Preliminary')
  pvtxt10.SetFillStyle(0)
  pvtxt10.SetBorderSize(0)
  pvtxt10.SetTextSize(0.03)
  pvtxt10.Draw()
  pvtxt9 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pvtxt9.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pvtxt9.SetFillStyle(0)
  pvtxt9.SetBorderSize(0)
  pvtxt9.SetTextSize(0.03)
  pvtxt9.Draw()

  canv.SaveAs("etaDistro.gif")
  canv.Close()

  print "----- Creating Second TCanvas -----"
  H = 800
  W = 800
  c = TCanvas("c", "Canvas",50,50,W,H)
  c.SetFillColor(0)
  c.SetBorderMode(0)
  c.SetFrameFillStyle(0)
  c.SetFrameBorderMode(0)
  c.SetLeftMargin( L/W )
  c.SetRightMargin( R/W )
  c.SetTopMargin( T/H )
  c.SetBottomMargin( B/H )
  c.SetTickx(0)
  c.SetTicky(0) 
  gPad.SetLogy()

  print " ------------ Creating TMultiGraph -----------"
  mg = TMultiGraph()
  mg.Add(gr0E,"AP")
  mg.Add(gr0W,"AP")
  mg.Add(gr7E,"AP")
  mg.Add(gr7W,"AP")
  mg.Add(gr1W,"AP")
  mg.Add(gr8W,"AP")
  mg.Draw("a")
  mg.SetTitle( 'RB1in')
  mg.GetXaxis().SetTitle( '#eta' )
  mg.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mg.SetMaximum(maxY)
  mg.GetXaxis().SetLabelFont(42)
  mg.GetXaxis().SetLabelOffset(0.007)
  mg.GetXaxis().SetLabelSize(0.043)
  mg.GetXaxis().SetTitleSize(0.05)
  mg.GetXaxis().SetTitleOffset(1.06)
  mg.GetXaxis().SetTitleFont(42)
  mg.GetYaxis().SetLabelFont(42)
  mg.GetYaxis().SetLabelOffset(0.008)
  mg.GetYaxis().SetLabelSize(0.05)
  mg.GetYaxis().SetTitleSize(0.06)
  mg.GetYaxis().SetTitleOffset(0.87)
  mg.GetYaxis().SetTitleFont(42)

  pvt = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pvt.AddText('CMS Preliminary')
  pvt.SetFillStyle(0)
  pvt.SetBorderSize(0)
  pvt.SetTextSize(0.03)
  pvt.Draw()
  pvt1 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pvt1.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pvt1.SetFillStyle(0)
  pvt1.SetBorderSize(0)
  pvt1.SetTextSize(0.03)
  pvt1.Draw()

  legenda = TLegend(0.4, 0.7, .7, .9)
  legenda.SetNColumns(1)
  legenda.AddEntry(gr0E, "RE1", "p")
  legenda.AddEntry(gr0W, "RB1in", "p")
  legenda.AddEntry(gr1W, "RB1out", "p")
  legenda.SetTextSize(0.05)
  legenda.Draw("a");

  c.SaveAs("etaDistroDetailRB1.png")
  c.Close()

  print "----- Creating Second TCanvas -----"
  c1 = TCanvas("c1", "Canvas",50,50,W,H)
  c1.SetFillColor(0)
  c1.SetBorderMode(0)
  c1.SetFrameFillStyle(0)
  c1.SetFrameBorderMode(0)
  c1.SetLeftMargin( L/W )
  c1.SetRightMargin( R/W )
  c1.SetTopMargin( T/H )
  c1.SetBottomMargin( B/H )
  c1.SetTickx(0)
  c1.SetTicky(0)
  gPad.SetLogy()

  print " ------------ Creating TMultiGraph -----------"
  mgd2 = TMultiGraph()
  mgd2.Add(gr3E,"AP")
  mgd2.Add(gr3W,"AP")
  mgd2.Add(gr10E,"AP")
  mgd2.Add(gr10W,"AP")
  mgd2.Add(gr4W,"AP")
  mgd2.Add(gr11W,"AP")
  mgd2.Draw("a")
  mgd2.SetTitle( 'RB1in')
  mgd2.GetXaxis().SetTitle( '#eta' )
  mgd2.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mgd2.SetMaximum(maxY)
  mgd2.GetXaxis().SetLabelFont(42)
  mgd2.GetXaxis().SetLabelOffset(0.007)
  mgd2.GetXaxis().SetLabelSize(0.043)
  mgd2.GetXaxis().SetTitleSize(0.05)
  mgd2.GetXaxis().SetTitleOffset(1.06)
  mgd2.GetXaxis().SetTitleFont(42)
  mgd2.GetYaxis().SetLabelFont(42)
  mgd2.GetYaxis().SetLabelOffset(0.008)
  mgd2.GetYaxis().SetLabelSize(0.05)
  mgd2.GetYaxis().SetTitleSize(0.06)
  mgd2.GetYaxis().SetTitleOffset(0.87)
  mgd2.GetYaxis().SetTitleFont(42)

  pv = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pv.AddText('CMS Preliminary')
  pv.SetFillStyle(0)
  pv.SetBorderSize(0)
  pv.SetTextSize(0.03)
  pv.Draw()
  pv1 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pv1.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pv1.SetFillStyle(0)
  pv1.SetBorderSize(0)
  pv1.SetTextSize(0.03)
  pv1.Draw()

  legendd2 = TLegend(0.4, 0.6, .7, .8)
  legendd2.SetNColumns(1)
  legendd2.AddEntry(gr3E, "RE2", "p")
  legendd2.AddEntry(gr3W, "RB2in", "p")
  legendd2.AddEntry(gr4W, "RB2out", "p")
  legendd2.SetTextSize(0.05)
  legendd2.Draw("a");

  c1.SaveAs("etaDistroDetailRB2.png")
  c1.Close() 

  print "----- Creating Third TCanvas -----"
  c3 = TCanvas("c3", "Canvas",50,50,W,H)
  c3.SetFillColor(0)
  c3.SetBorderMode(0)
  c3.SetFrameFillStyle(0)
  c3.SetFrameBorderMode(0)
  c3.SetLeftMargin( L/W )
  c3.SetRightMargin( R/W )
  c3.SetTopMargin( T/H )
  c3.SetBottomMargin( B/H )
  c3.SetTickx(0)
  c3.SetTicky(0)
  gPad.SetLogy()

  print " ------------ Creating TMultiGraph -----------"
  List = generateDTTGraphs.main()
  print List
  ListCSC = generateCSCTGraphs.main() 
  print ListCSC
  
  mgd3 = TMultiGraph()
  mgd3.Add(gr3E,"AP")
  mgd3.Add(gr3W,"AP")
  mgd3.Add(gr10E,"AP")
  mgd3.Add(gr10W,"AP")
  mgd3.Add(gr4W,"AP")
  mgd3.Add(gr11W,"AP")
  mgd3.Add(List[1],"AP")
  mgd3.Add(ListCSC[1],"AP")
  mgd3.Draw("a")
  mgd3.SetTitle( 'RB1in')
  mgd3.GetXaxis().SetTitle( '#eta' )
  mgd3.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mgd3.SetMaximum(maxY)
  mgd3.GetXaxis().SetLabelFont(42)
  mgd3.GetXaxis().SetLabelOffset(0.007)
  mgd3.GetXaxis().SetLabelSize(0.043)
  mgd3.GetXaxis().SetTitleSize(0.05)
  mgd3.GetXaxis().SetTitleOffset(1.06)
  mgd3.GetXaxis().SetTitleFont(42)
  mgd3.GetYaxis().SetLabelFont(42)
  mgd3.GetYaxis().SetLabelOffset(0.008)
  mgd3.GetYaxis().SetLabelSize(0.05)
  mgd3.GetYaxis().SetTitleSize(0.06)
  mgd3.GetYaxis().SetTitleOffset(0.87)
  mgd3.GetYaxis().SetTitleFont(42)

  pv03 = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pv03.AddText('CMS Preliminary')
  pv03.SetFillStyle(0)
  pv03.SetBorderSize(0)
  pv03.SetTextSize(0.03)
  pv03.Draw()
  pv103 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pv103.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pv103.SetFillStyle(0)
  pv103.SetBorderSize(0)
  pv103.SetTextSize(0.03)
  pv103.Draw()

  legendd3 = TLegend(0.4, 0.6, .7, .8)
  legendd3.SetNColumns(1)
  legendd3.AddEntry(gr3E, "RE2", "p")
  legendd3.AddEntry(gr3W, "RB2in", "p")
  legendd3.AddEntry(gr4W, "RB2out", "p")
  legendd3.AddEntry(List[1], "MB2", "p")
  legendd3.AddEntry(ListCSC[1], "ME2", "p")
  legendd3.SetTextSize(0.05)
  legendd3.Draw("a");

  c3.SaveAs("etaDistroDetailRB2withDT.png")
  c3.Close()

  print "----- Creating Fourth TCanvas -----"
  c4 = TCanvas("c4", "Canvas",50,50,W,H)
  c4.SetFillColor(0)
  c4.SetBorderMode(0)
  c4.SetFrameFillStyle(0)
  c4.SetFrameBorderMode(0)
  c4.SetLeftMargin( L/W )
  c4.SetRightMargin( R/W )
  c4.SetTopMargin( T/H )
  c4.SetBottomMargin( B/H )
  c4.SetTickx(0)
  c4.SetTicky(0)
  gPad.SetLogy()

  print " ------------ Creating TMultiGraph -----------"
  mgd4 = TMultiGraph()
  mgd4.Add(gr5E,"AP")
  mgd4.Add(gr5W,"AP")
  mgd4.Add(gr12E,"AP")
  mgd4.Add(gr12W,"AP")
  mgd4.Add(List[2],"AP")
  mgd4.Add(ListCSC[2],"AP")
  mgd4.Draw("a")
  mgd4.SetTitle( 'RB3')
  mgd4.GetXaxis().SetTitle( '#eta' )
  mgd4.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mgd4.SetMaximum(maxY)
  mgd4.GetXaxis().SetLabelFont(42)
  mgd4.GetXaxis().SetLabelOffset(0.007)
  mgd4.GetXaxis().SetLabelSize(0.043)
  mgd4.GetXaxis().SetTitleSize(0.05)
  mgd4.GetXaxis().SetTitleOffset(1.06)
  mgd4.GetXaxis().SetTitleFont(42)
  mgd4.GetYaxis().SetLabelFont(42)
  mgd4.GetYaxis().SetLabelOffset(0.008)
  mgd4.GetYaxis().SetLabelSize(0.05)
  mgd4.GetYaxis().SetTitleSize(0.06)
  mgd4.GetYaxis().SetTitleOffset(0.87)
  mgd4.GetYaxis().SetTitleFont(42)

  pv04 = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pv04.AddText('CMS Preliminary')
  pv04.SetFillStyle(0)
  pv04.SetBorderSize(0)
  pv04.SetTextSize(0.03)
  pv04.Draw()
  pv104 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pv104.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pv104.SetFillStyle(0)
  pv104.SetBorderSize(0)
  pv104.SetTextSize(0.03)
  pv104.Draw()

  legendd4 = TLegend(0.4, 0.6, .7, .8)
  legendd4.SetNColumns(1)
  legendd4.AddEntry(gr5E, "RE3", "p")
  legendd4.AddEntry(gr5W, "RB3", "p")
  legendd4.AddEntry(List[2], "MB3", "p")
  legendd4.AddEntry(ListCSC[2], "ME3", "p")
  legendd4.SetTextSize(0.05)
  legendd4.Draw("a");

  c4.SaveAs("etaDistroDetailRB3withDT.png")
  c4.Close()

  print "----- Creating Fifth TCanvas -----"
  c5 = TCanvas("c5", "Canvas",50,50,W,H)
  c5.SetFillColor(0)
  c5.SetBorderMode(0)
  c5.SetFrameFillStyle(0)
  c5.SetFrameBorderMode(0)
  c5.SetLeftMargin( L/W )
  c5.SetRightMargin( R/W )
  c5.SetTopMargin( T/H )
  c5.SetBottomMargin( B/H )
  c5.SetTickx(0)
  c5.SetTicky(0)
  gPad.SetLogy()

  print " ------------ Creating TMultiGraph -----------"
  mgd5 = TMultiGraph()
  mgd5.Add(gr6E,"AP")
  mgd5.Add(gr6W,"AP")
  mgd5.Add(gr13E,"AP")
  mgd5.Add(gr13W,"AP")
  mgd5.Add(List[3],"AP")
  mgd5.Add(ListCSC[3],"AP")
  mgd5.Draw("a")
  mgd5.SetTitle( 'RB4')
  mgd5.GetXaxis().SetTitle( '#eta' )
  mgd5.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mgd5.SetMaximum(maxY)
  mgd5.GetXaxis().SetLabelFont(42)
  mgd5.GetXaxis().SetLabelOffset(0.007)
  mgd5.GetXaxis().SetLabelSize(0.043)
  mgd5.GetXaxis().SetTitleSize(0.05)
  mgd5.GetXaxis().SetTitleOffset(1.06)
  mgd5.GetXaxis().SetTitleFont(42)
  mgd5.GetYaxis().SetLabelFont(42)
  mgd5.GetYaxis().SetLabelOffset(0.008)
  mgd5.GetYaxis().SetLabelSize(0.05)
  mgd5.GetYaxis().SetTitleSize(0.06)
  mgd5.GetYaxis().SetTitleOffset(0.87)
  mgd5.GetYaxis().SetTitleFont(42)

  pv05 = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pv05.AddText('CMS Preliminary')
  pv05.SetFillStyle(0)
  pv05.SetBorderSize(0)
  pv05.SetTextSize(0.03)
  pv05.Draw()
  pv105 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pv105.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pv105.SetFillStyle(0)
  pv105.SetBorderSize(0)
  pv105.SetTextSize(0.03)
  pv105.Draw()

  legendd5 = TLegend(0.4, 0.7, .7, .9)
  legendd5.SetNColumns(1)
  legendd5.AddEntry(gr6E, "RE4", "p")
  legendd5.AddEntry(gr6W, "RB4", "p")
  legendd5.AddEntry(List[3], "MB4", "p")
  legendd5.AddEntry(ListCSC[3], "ME4", "p")
  legendd5.SetTextSize(0.05)
  legendd5.Draw("a");

  c5.SaveAs("etaDistroDetailRB4withDT.png")
  c5.Close()

  print "----- Creating Sixth TCanvas -----"
  c6 = TCanvas("c3", "Canvas",50,50,W,H)
  c6.SetFillColor(0)
  c6.SetBorderMode(0)
  c6.SetFrameFillStyle(0)
  c6.SetFrameBorderMode(0)
  c6.SetLeftMargin( L/W )
  c6.SetRightMargin( R/W )
  c6.SetTopMargin( T/H )
  c6.SetBottomMargin( B/H )
  c6.SetTickx(0)
  c6.SetTicky(0)
  gPad.SetLogy()

  print " ------------ Creating TMultiGraph -----------"

  List[0].SetMarkerColor( kGreen+3 )
  List[0].SetMarkerStyle( 21 )
  ListCSC[0].SetMarkerColor( kRed+3 )
  ListCSC[0].SetMarkerStyle( 21 )

  mgd6 = TMultiGraph()
  mgd6.Add(gr0E,"AP")
  mgd6.Add(gr0W,"AP")
  mgd6.Add(gr7E,"AP")
  mgd6.Add(gr7W,"AP")
  mgd6.Add(gr1W,"AP")
  mgd6.Add(gr8W,"AP")
  mgd6.Add(List[0],"AP")
  mgd6.Add(ListCSC[0],"AP")
  mgd6.Draw("a")
  mgd6.SetTitle( 'RB1in')
  mgd6.GetXaxis().SetTitle( '#eta' )
  mgd6.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mgd6.SetMaximum(maxY)
  mgd6.GetXaxis().SetLabelFont(42)
  mgd6.GetXaxis().SetLabelOffset(0.007)
  mgd6.GetXaxis().SetLabelSize(0.043)
  mgd6.GetXaxis().SetTitleSize(0.05)
  mgd6.GetXaxis().SetTitleOffset(1.06)
  mgd6.GetXaxis().SetTitleFont(42)
  mgd6.GetYaxis().SetLabelFont(42)
  mgd6.GetYaxis().SetLabelOffset(0.008)
  mgd6.GetYaxis().SetLabelSize(0.05)
  mgd6.GetYaxis().SetTitleSize(0.06)
  mgd6.GetYaxis().SetTitleOffset(0.87)
  mgd6.GetYaxis().SetTitleFont(42)

  pv06 = TPaveText(.1,0.97,.55,0.97,"NDC") #(.06,.4,.55,.73)
  pv06.AddText('CMS Preliminary')
  pv06.SetFillStyle(0)
  pv06.SetBorderSize(0)
  pv06.SetTextSize(0.03)
  pv06.Draw()
  pv106 = TPaveText(.7,0.97,.9,0.97,"NDC")
  pv106.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pv106.SetFillStyle(0)
  pv106.SetBorderSize(0)
  pv106.SetTextSize(0.03)
  pv106.Draw()

  legendd6 = TLegend(0.4, 0.7, .7, .9)
  legendd6.SetNColumns(1)
  legendd6.AddEntry(gr0E, "RE1", "p")
  legendd6.AddEntry(gr0W, "RB1in", "p")
  legendd6.AddEntry(gr1W, "RB1out", "p")
  legendd6.AddEntry(List[0], "MB1", "p")
  legendd6.AddEntry(ListCSC[0], "ME1", "p")
  legendd6.SetTextSize(0.05)
  legendd6.Draw("a");

  c6.SaveAs("etaDistroDetailRB1withDT.png")
  c6.Close()

  
  print "is there an error here?"
  return

##
##
if __name__ == "__main__":
  endcapSectionList = ["RE-1", "RE-1", "RE-2", "RE-2", "RE-2", "RE-3", "RE-4", "RE+1", "RE+1","RE+2", "RE+2", "RE+2", "RE+3", "RE+4"]
  wheelSectionList  = ["RB1in", "RB1out", "RB2", "RB2in", "RB2out", "RB3", "RB4", "RB1in", "RB1out", "RB2", "RB2in", "RB2out", "RB3", "RB4"]
  wheelSectionList0 = ["-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "+", "+", "+", "+"]
  endcapSection = "RE+4" # default value
  wheelSection  = "RB4"  # default value
  wheelSection0 = "-"    # default value

  xW, yW = [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  xE, yE = [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for i in range(len(xW)):
    endcapSection = endcapSectionList[i]
    wheelSection  = wheelSectionList[i]
    wheelSection0 = wheelSectionList0[i]
    xW[i], yW[i], xE[i], yE[i] = main()
  print "does it break right here?"

  eta_plot(xW[0],yW[0],xW[1],yW[1],xW[2],yW[2],xW[3] ,yW[3], xW[4], yW[4], xW[5], yW[5], xW[6], yW[6],
           xW[7],yW[7],xW[8],yW[8],xW[9],yW[9],xW[10],yW[10],xW[11],yW[11],xW[12],yW[12],xW[13],yW[13],
           xE[0],yE[0],xE[1],yE[1],xE[2],yE[2],xE[3] ,yE[3], xE[4], yE[4], xE[5], yE[5], xE[6], yE[6],
           xE[7],yE[7],xE[8],yE[8],xE[9],yE[9],xE[10],yE[10],xE[11],yE[11],xE[12],yE[12],xE[13],yE[13])
  print "nah, it breaks after the plotting function... somehow?"  


