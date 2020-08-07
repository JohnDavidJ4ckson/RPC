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
import ROOT as rt
import CMS_lumi, tdrstyle
#import RPCRates

## Null -> List[eta, wheel, station, section]
## The function takes the fixed geometry file
## and uses it to produce a list with the eta
## value for each corresponding part of the DT
## detector.
def eta_list():
  lines = []
  with open('GeometryDT.out', 'rw') as shakes:
    for line in shakes:
      l = re.compile("( *)").split(line)
      lines.append(l)
  name = []
  eta = []
  wheel = []
  station = []
  section = []
  phi = []
  #i = 1
  for line in lines:
#########################
# Testing prints should be commented when running
#########################
    phiStrings = line[-1].rstrip()
    etaStrings = line[-3]
    etaWheel   = line[0]
    etaStation = line[2]
    etaSection = line[4]
    #print i, etaStrings, etaWheel, etaStation, etaSection
    #i += 1
#########################
    phiValue     = float(line[-1].split("=")[-1])
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
    phiDegrees = phiValue * (180/3.14159265359)
    if phiDegrees < -10.0: phiDegrees = 360+phiDegrees
    phi.append(phiDegrees)  #phiValue)
#  print eta
#  print wheel
#  print station
#  print section
#  print phi
  return eta, wheel, station, section, phi
#  print name


## Null -> List[eta, wheel, station, section]
## The function takes the fixed geometry file
## and uses it to produce a list with the rates
## value for each corresponding part of the DT
## detector.
def rates_list():
  lines = []
  with open('DTrates2018Corrected.txt', 'rw') as shakes:
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
#    print i, rateStrings, rateWheel, rateStation, rateSection
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
#  print rate
#  print wheel
#  print station
#  print section
  return rate, wheel, station, section


## Null -> List
## This function gathers the info of both eta and rates 
## then summs it up into a list of dictionaries
def the_list():
  eta, wh_eta, st_eta, se_eta, phi = eta_list()
  rates, wh_ra, st_ra, se_ra  = rates_list()
  theList = []
  theDict = {}
  for i in eta:
    etaIndex = eta.index(i)
    for j in rates:
      ratesIndex = rates.index(j)
      if wh_eta[etaIndex] == wh_ra[ratesIndex] and st_eta[etaIndex] == st_ra[ratesIndex] and se_eta[etaIndex] == se_ra[ratesIndex]:
        #print "got it, eta =  "+str(i)+" matches with rates = "+str(j)
        indict = { "wheel": wh_eta[etaIndex],
                   "station": st_eta[etaIndex],
                   "section": se_eta[etaIndex],
                   "eta": i,
                   "rates": j,
                   "phi": phi[etaIndex]}
        #print indict
        theList.append(indict)
#  print len(theList)
  return theList

## list -> dictionary
## The function takes the list that has the information about phi, rates, and the
## station-wheel-section of the DT. The function creates an standard key, e.g.
## W-2_MB4_S01 and assigns a dictionary with the rate and phi to each key.
def the_dictionary(lista):
  stations = ["MB1","MB2","MB3", "MB4"]
  wheels = ["-2", "-1", "+0", "+1", "+2"]
  chambers = [
             "01","02","03","04","05","06",
             "07","08","09","10","11","12"]
  theDict = {}
  for e in lista:
    for w in wheels:
      if e["wheel"] == float(w):
        wheelName = 'W'+w
        #print wheelName
    statName = ""
    for st in stations:
      if e["station"] == float(st[-1]):
        statName = st
        #print statName
    for c in chambers: 
      if e["section"] == float(c): 
        sectName = 'S'+c
        #print sectName
    name = wheelName+"_"+statName+"_"+sectName
    #print name
    indict = { "phi":e["phi"],
               "rates":e["rates"]}
    theDict[name] = indict
  #print theDict
  return theDict

## dictionary -> dictionary
## This function takes the dictionary with the correct granularity and
## keys similar to W+2_RB3_S03. The chambers are used as the inputs of
## TGraphs. In the end a new dictionary is returned with a TGraphs 
## and with a key similar to W+2_RB3.
def generate_tgraphs(dict0):
  stations = ["MB1", "MB2", "MB3", "MB4"]
  wheels = ["-2", "-1", "+0", "+1", "+2"]
  chambers = [
             "01","02","03","04","05","06",
             "07","08","09","10","11","12"]
  grDict = {}
  for w in wheels:
    for s in stations:
    #Create lists to average here
      name = "W"+w+"_"+s
      xMB1, xMB2, xMB3, xMB4 = array('d'),array('d'),array('d'),array('d')
      yMB1, yMB2, yMB3, yMB4 = array('d'),array('d'),array('d'),array('d')
      xlist = [xMB1, xMB2, xMB3, xMB4]
      ylist = [yMB1, yMB2, yMB3, yMB4]
      for k,v in dict0.items():
        for c in chambers:
          if k == "W"+w+"_"+s+"_S"+c:
            stationIndex = stations.index(s)
            #print stationIndex
            xlist[stationIndex].append(v["phi"])
            ylist[stationIndex].append(v["rates"])
      tgr  = create_tgraphs(xlist[stationIndex],ylist[stationIndex],name)
      #print name
      #print tgr       
      grDict[name] = tgr
  return grDict


## array, array, string -> TGraph
## The function recieves an x and y values to create
## a tgraph of them with the given name.
## This function is imported for use in the etaDistro.py file
def create_tgraphs(x, y, name):
  #print "------ Creating Wheel TGraph for "+name+"----------"
  n = len(x)
  gr = TGraph(n,x,y)
  gr.SetMarkerColor( kGreen+3 )
  gr.SetMarkerStyle( 20 )
  gr.SetMarkerSize( 1.5 )
  gr.SetLineColor( 5 )
  gr.SetLineWidth( 7 )
  gr.SetTitle( name )
  gr.GetXaxis().SetTitle( '#eta' )
  gr.GetYaxis().SetTitle( 'DT single hit rate (Hz/cm^{2})' )
  return gr

## list -> Null
## The function produces and saves the plot of the DT rates over phi distribution
def plotDT_phi(listOf, layer):
  List = listOf
  H = 1600
  W = 800
  #print "----- Creating TCanvas -----"
  c = TCanvas("c", "Canvas",W,H)
  #c.Divide(2)
  ymax = 0.0

  #c.cd(1)
  c.SetLeftMargin(0.15);
  c.SetRightMargin(0.06);
  c.SetTopMargin(0.09);
  c.SetBottomMargin(0.14);
  gPad.SetGrid()
  gPad.SetLogy()

  #c.SetFillColor(0)
  #c.SetBorderMode(0)
  #c.SetFrameFillStyle(0)
  #c.SetFrameBorderMode(0)
  #c.SetTickx(0)
  #c.SetTicky(0)
  for gr in List:
    if ymax < gr.GetMaximum():
      ymax = gr.GetMaximum()
    gr.SetMarkerColor(2)
    gr.SetMaximum(300)
#    gr.Draw("p same hist")
#    gr.SetStats(0)

  #print " ------------ Creating TMultiGraph -----------"
  List[0].SetMarkerStyle(26)
  List[1].SetMarkerStyle(20)
  List[2].SetMarkerStyle(25)
  List[3].SetMarkerStyle(23)


  #maxY = 12
  mg = TMultiGraph()
  mg.Add(List[0],"AP")
  mg.Add(List[1],"AP")
  mg.Add(List[2],"AP")
  mg.Add(List[3],"AP")
  mg.Draw("a")
  mg.SetTitle( layer)
  mg.GetXaxis().SetTitle( '#phi' )
  mg.GetYaxis().SetTitle( 'DT single hit rate (Hz/cm^{2})' )
  mg.SetMaximum(ymax)
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

  pv = TPaveText(.08,0.97,.45,0.97,"NDC") 
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
  l = TLegend(0.25,0.20,0.75,0.30)
  l.SetFillColor(0)
  l.SetBorderSize(0)
  l.SetTextSize(0.03)
  l.SetNColumns(4)
  l.AddEntry(List[0], "MB1", "p")
  l.AddEntry(List[1], "MB2", "p")
  l.AddEntry(List[2], "MB3", "p")
  l.AddEntry(List[3], "MB4", "p")
  #l.SetTextSize(0.05)
  l.Draw("a");

  c.SaveAs("phiDistroDT{}.png".format(layer))
#  variable = RPCRates.inPhi()
#  print variable

def main():
  #print "Creating the list from geometry and rates info"
  list0 = the_list()
  #print "Creating the dictionary with the standard names"
  dict0 = the_dictionary(list0)
  #return dict0  ######## Comment this return in order to print all the plots for DT 
  #print "Creating the dictionary with TGraph objects"
  dict1 = generate_tgraphs(dict0)
  print "Do we really need the plots?"
  print dict1
  print "Creating plots"

  wheels = ["W-2", "W-1", "W+0", "W+1", "W+2"]
  for w in wheels:
    tgraphList = [ dict1[k] for k,v in dict1.items() if w in k]
    plotDT_phi(tgraphList, "Wheel"+w[-2]+w[-1])
  print "DONE"
  print dict1
  return dict1

if __name__ == "__main__":
  main()
