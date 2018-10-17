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
#import RPCRates
from numpy import isnan
import csv


## Value -> Boolean
## This function returns True if the given object is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

## Null -> dictionary
## The function uses a fixed json file to return a dictionary with
## RPC Id names as keys and the corresponding rates in the entry. 
## The IDnames are createad in the form RE+4_R2_CH09_A 
def rates_endcap_list(data):
  runNumfile = data  #"run322619/output_rolls.json" #"output_rolls2018.json"
  with open(runNumfile, 'rb') as csvfile: 
    current = []
    lumi = []
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      if not row: continue
      #print row
      curry = float(row[1])
      lummo = float(row[2])
      current.append(curry)
      lumi.append(lummo)
  #print current
  #print lumi

  return [current, lumi]

  rolls = ["_A","_B","_C"] #, "_D"]
  chambers = [
             "01","02","03","04","05","06","07","08","09",
        "10","11","12","13","14","15","16","17","18","19",
        "20","21","22","23","24","25","26","27","28","29",
        "30","31","32","33","34","35","36"
        ]
  ring = ["_R2", "_R3"]
  endcap = ["+4", "-4"]
  names = []
  rates = []
  theDict = {}
  for e in endcap:
    for r in ring:
      for roll in rolls:
        #rates = []
        for c in chambers:
          try:
            #print r
            if float(rates1["rate"]["RE"+e+r+"_CH"+c+roll]["ratesquarecm"]) == 0: continue
            rates.append(float(rates1["rate"]["RE"+e+r+"_CH"+c+roll]["ratesquarecm"]))
            names.append("RE"+e+r+"_CH"+c+roll)
            theDict["RE"+e+r+"_CH"+c+roll] = float(rates1["rate"]["RE"+e+r+"_CH"+c+roll]["ratesquarecm"])
          except KeyError:
            continue
  #print sorted(names)
  return [names, rates]
  #return theDict

## Null ->  List of lists [string, double]
## The function uses a fixed txt file with the geometric information
## of the RPC's in the endcaps and returns a list of names and their
## corresponding pseudorapidity mean location.
def phi_endcap_list():
  lines = []
  with open('endcapGeometryRPC.out', 'rw') as shakes:
    for line in shakes:
      y = line.split(",")
      lines.append(y)
  name = []
  phiAvg = []
  for line in lines:
    nameList = line[0]
    name.append(nameList.rstrip())
    minPhiList = line[-2].split(" ")
    minPhiValue = float( minPhiList[-1] )  
    maxPhiList = line[-1].split(" ")
    maxPhiValue = float( maxPhiList[-2] ) 
    avgPhiValue = (minPhiValue + maxPhiValue) / 2
    if avgPhiValue < 0: phiFromZero = avgPhiValue + 6.28318530718
    else: phiFromZero = avgPhiValue 
    phiDegrees = phiFromZero * (360 / 6.28318530718)
    phiAvg.append(phiDegrees)
  List = [name, phiAvg]
  return List

## List of lists [string, double], 
## List of lists [string, double]  -> Dictionary
## The function maps the rates and pseudorapidities that share ID 
## names to each other and returns them in a dictionary
def the_list(phiList, ratesList):
  intersect = set(phiList[0]).intersection(ratesList[0])
  #print len(intersect)
  dict0 = {}
  for i in intersect:
    etaIndex = phiList[0].index(i)
    rateIndex = ratesList[0].index(i)
    indict = { "phi": phiList[1][etaIndex],
               "rates":ratesList[1][rateIndex] }
    dict0[i] = indict
  return dict0

## array, array, string -> TGraph
## The function recieves an x and y values to create
## a tgraph of them with the given name.
## This function is imported for use in the etaDistro.py file
def create_tgraphs(x, y, name):
  #print "------ Creating Wheel TGraph of "+name+"----------"
  n = len(x)
  gr = TGraph(n,x,y)
  gr.SetMarkerColor( kGreen+3 )
  gr.SetMarkerStyle( 20 )
  gr.SetMarkerSize( 1.5 )
  gr.SetLineColor( 5 )
  gr.SetLineWidth( 7 )
  gr.SetTitle( name )
  gr.GetXaxis().SetTitle( '#phi' )
  gr.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  return gr

## dictionary -> dictionary
## The function takes a dictionary that has the information about phi, rates, and the
## Id/key of the RPC detector e.g. W+2_RB3-_S03_Forward
## The function avarages over subrolls and rings such that the output key has the form
## W+2_RB3_S03 and can be used for TGraph filling
def granularity_average(dictionary):
  rolls = ["_A","_B","_C"] #, "_D"]
  chambers = [
             "01","02","03","04","05","06","07","08","09",
        "10","11","12","13","14","15","16","17","18","19",
        "20","21","22","23","24","25","26","27","28","29",
        "30","31","32","33","34","35","36"
        ]
  ring = ["_R2", "_R3"]
  endcap = ["+4", "-4"]
  dict0 = {}
  for e in endcap:
    for c in chambers: 
      #Create lists to extract averages here
      names = []
      phi = []
      rates = []
      for k, v in dictionary.items():
        for ri in ring:
          for r in rolls:
            if k == "RE"+e+ri+"_CH"+c+r: 
              names.append(k)
              cleanPhi = v["phi"]
              rates.append( v["rates"] )
              name = "RE"+e+"_CH"+c
              if c == "19": cleanPhi = 180
              if (c == "01" and cleanPhi > 300): cleanPhi -= 360
              phi.append(cleanPhi)
      try:
        phiAvg   = sum(phi)/len(phi)
        ratesAvg = sum(rates)/len(rates)
        #print name, phiAvg, ratesAvg
        #print "The phi list is ", phi
        indict = { "phi":phiAvg,
             "rates":ratesAvg }
        dict0[name] = indict
      except ZeroDivisionError:
        continue
  return dict0

## dictionary -> dictionary
## This function takes the dictionary with the correct granularity and
## keys similar to W+2_RB3_S03. The chambers are used as the inputs of
## TGraphs. In the end a new dictionary is returned with a TGraphs 
## and with a key similar to W+2_RB3.
def generate_tgraphs(dict0,name):
  xRE4 = array('d')
  yRE4 = array('d')
  for e in dict0[0]:
    yRE4.append(e)
  for e in dict0[1]:
    xRE4.append(e)
  tgr  = create_tgraphs(xRE4,yRE4,name)
  print tgr


  return tgr 

  chambers = [
             "01","02","03","04","05","06","07","08","09",
        "10","11","12","13","14","15","16","17","18","19",
        "20","21","22","23","24","25","26","27","28","29",
        "30","31","32","33","34","35","36"
        ]
  endcap = ["+4", "-4"]
  
  grDict = {}
  for e in endcap:
    #Create lists to average here
    name = "RE"+e
    xRB1, xRB2, xRB3, xRB4 = array('d'),array('d'),array('d'),array('d')
    yRB1, yRB2, yRB3, yRB4 = array('d'),array('d'),array('d'),array('d')
    xlist = [xRB1, xRB2, xRB3, xRB4]
    ylist = [yRB1, yRB2, yRB3, yRB4]
    for k,v in dict0.items():
      for c in chambers:
        if k == "RE"+e+"_CH"+c:
          stationIndex = endcap.index(e)
          #print stationIndex
          xlist[stationIndex].append(v["phi"])
          ylist[stationIndex].append(v["rates"])
    tgr  = create_tgraphs(xlist[stationIndex],ylist[stationIndex],name)
    #print name
    #print tgr       
    grDict[name] = tgr
  return grDict

## list, string --> Nul
## The function receives a list with TGraphs for each RPC Layer
## and the name of a wheel. These are used to create a plot 
def plot_results(List, layer):
  H = 1600
  W = 800
  #print "----- Creating Third TCanvas -----"
  c = TCanvas("c", "Canvas",W,H)
  ymax = 0.0
  c.SetLeftMargin(0.15);
  c.SetRightMargin(0.06);
  c.SetTopMargin(0.09);
  c.SetBottomMargin(0.14);
  gPad.SetGrid()
  gPad.SetLogy()
  for gr in List:
    if ymax < max(gr.GetY()):
      ymax = max(gr.GetY())
    gr.SetMarkerColor(2)
    #print "The TGraph has this number of elements"
    #print gr.GetN()
    #gr.SetMaximum(300)
    #gr.Draw("p same hist")
    #gr.SetStats(0)

  #print " ------------ Creating TMultiGraph -----------"
  List[0].SetMarkerColor( kBlue+2 )
  #List[0].SetMarkerStyle( 21 )
  List[1].SetMarkerColor( kRed+2 )
  #List[1].SetMarkerStyle( 22 )
  #List[2].SetMarkerColor( kBlue )
  #List[3].SetMarkerStyle( 23 )
  #List[3].SetMarkerColor( kBlue+2 )
  List[0].SetMarkerStyle(20)
  List[1].SetMarkerStyle(23)
  #List[2].SetMarkerStyle(25)
  #List[3].SetMarkerStyle(23)

  #maxY = 12
  mg = TMultiGraph()
  mg.Add(List[0],"AP")
  mg.Add(List[1],"AP")
  #mg.Add(List[2],"AP")
  #mg.Add(List[3],"AP")
  mg.Draw("a")
  mg.SetTitle( "")
  mg.GetXaxis().SetTitle( 'Luminosity "online_luminosity_m1"' )
  mg.GetYaxis().SetTitle( 'Current "imon"' )
  mg.SetMaximum(ymax*3)
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
  mg.GetYaxis().SetTitleOffset(0.98)
  mg.GetYaxis().SetTitleFont(42)

  pv = TPaveText(.08,0.93,.45,0.93,"NDC") 
  pv.AddText('CMS Preliminary')
  pv.SetFillStyle(0)
  pv.SetBorderSize(0)
  pv.SetTextSize(0.03)
  pv.Draw()
  pv1 = TPaveText(.7,0.97,.9,0.97,"NDC")
  #pv1.AddText('1.5 #times 10^{34} Hz/cm^{2} (13 TeV)')
  pv1.SetFillStyle(0)
  pv1.SetBorderSize(0)
  pv1.SetTextSize(0.03)
  pv1.Draw()
  l = TLegend(0.25,0.78,0.75,0.88)
  l.SetFillColor(0)
  l.SetBorderSize(0)
  l.SetTextSize(0.03)
  l.SetNColumns(1)
  l.AddEntry(List[0], "RE+4 runs from 2018.08.10 until 2018.09.10  (before TS2)", "p")
  l.AddEntry(List[1], "RE+4 runs from 2018.09.15 until 2018.10.07  (after TS2)", "p")
  #l.AddEntry(List[2], "RE-4 run 322355 (before TS2)", "p")
  #l.AddEntry(List[3], "RE+4 run 322355 (before TS2)", "p")
  #l.SetTextSize(0.05)
  l.Draw("a");

  c.SaveAs("currentDistroRPC{}.png".format(layer))

## Null -> Null
## The main function uses the rest of functions to create a TGraph dictionary
## in the agreed granularity then distribute it to the plotting function.
def main():
  print "Retrieving rates Info"
  listaRatesAfterTS2 =  rates_endcap_list("RE+4afterTS2/outputs/lhcfill_RE+4afterTS2.csv")
  listaRatesBeforeTS2 = rates_endcap_list("RE+4beforeTS2/outputs/lhcfill_RE+4beforeTS2.csv")

  print "Generating TGraphs"
  print "THIS is AFTER"
  tgraphsDictionaryAfterTS2  = generate_tgraphs(listaRatesAfterTS2,'RE+4 after TS2')
  print "THIS is BEFORE"
  tgraphsDictionaryBeforeTS2 = generate_tgraphs(listaRatesBeforeTS2,'RE+4 before TS2')

  print "Creating plots"
  tgraphList = [ tgraphsDictionaryBeforeTS2, tgraphsDictionaryAfterTS2 ]
  plot_results(tgraphList, "RE+4 Comparison")
  print "DONE"


  return
  print "Retrieving rates Info"
  listaPhi = phi_endcap_list()
  print "Creating phi-rates-id dictionary"
  dictionary0AfterTS2  = the_list(listaPhi,listaRatesAfterTS2)
  dictionary0BeforeTS2 = the_list(listaPhi,listaRatesBeforeTS2)
  print "Taking the granularity average"
  dictionary1AfterTS2  = granularity_average(dictionary0AfterTS2)
  dictionary1BeforeTS2 = granularity_average(dictionary0BeforeTS2)
  ##return dictionary1
  print "Generating TGraphs"
  tgraphsDictionaryAfterTS2  = generate_tgraphs(dictionary1AfterTS2)
  tgraphsDictionaryBeforeTS2 = generate_tgraphs(dictionary1BeforeTS2)
  print tgraphsDictionaryAfterTS2
  print tgraphsDictionaryBeforeTS2
  ##return tgraphsDictionary #Use this return for the ratio plotting script
  print "Creating plots"
  tgraphList = [ tgraphsDictionaryAfterTS2["RE-4"], tgraphsDictionaryAfterTS2["RE+4"], 
                 tgraphsDictionaryBeforeTS2["RE-4"], tgraphsDictionaryBeforeTS2["RE+4"] ]
  plot_results(tgraphList, "endcapComparison") 
  print "DONE"
  ##return tgraphsDictionary #Use this return for the ratio plotting script

if __name__ == "__main__":
  main()

