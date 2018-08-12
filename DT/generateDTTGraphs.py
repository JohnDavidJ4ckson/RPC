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


## Null -> List[eta, wheel, station, section]
## The function takes the fixed geometry file
## and uses it to produce a list with the eta
## value for each corresponding part of the DT
## detector.
def eta_list():
  lines = []
  with open('Geometry.out', 'rw') as shakes:
    for line in shakes:
      l = re.compile("( *)").split(line)
      lines.append(l)
  name = []
  eta = []
  wheel = []
  station = []
  section = []
  #i = 1
  for line in lines:
#########################
# Testing prints should be commented when running
#########################
    etaStrings = line[-3]
    etaWheel   = line[0]
    etaStation = line[2]
    etaSection = line[4]
    #print i, etaStrings, etaWheel, etaStation, etaSection
    #i += 1
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
#  print eta
#  print wheel
#  print station
#  print section
  return eta, wheel, station, section
#  print name


## Null -> List[eta, wheel, station, section]
## The function takes the fixed geometry file
## and uses it to produce a list with the rates
## value for each corresponding part of the DT
## detector.
def rates_list():
  lines = []
  with open('DTrates2017.txt', 'rw') as shakes:
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
  eta, wh_eta, st_eta, se_eta = eta_list()
  rates, wh_ra, st_ra, se_ra  = rates_list()
  theList = []
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
                   "rates": j}
        #print indict
        theList.append(indict)
#  print len(theList)
  return theList

def plot_eta(x, y, name):
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

  print "----- Creating TCanvas -----"
  H = 800
  W = 1600
  canv = TCanvas("c1", "Canvas",50,50,W,H)
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
  #canv.Divide(3,2,0.001,0.001)
  CMS_lumi.CMS_lumi(canv, iPeriod, iPos)
  canv.cd()
  canv.Update()
  maxY = max(y)*1.5
  canv.cd(1)
  gPad.SetLogy()

  print "------ Creating Wheel TGraph ----------"
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


  print " ------------ Creating TMultiGraph -----------"
  mg = TMultiGraph()
  mg.Add(gr,"AP")
  mg.Draw("a")
  mg.SetTitle( name )
  mg.GetXaxis().SetTitle( '#eta' )
  mg.GetYaxis().SetTitle( 'DT single hit rate (Hz/cm^{2})' )
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

  l = TLegend(0.4, 0.6, .7, .8)
  l.SetNColumns(1)
  l.AddEntry(gr, name, "p")
  l.SetTextSize(0.05)
  l.Draw("a")

  canv.SaveAs("etaDistro{}.png".format(name))
  canv.Close()

def create_tgraphs(x, y, name):
  print "------ Creating Wheel TGraph ----------"
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


def main():
  a = the_list()
  xMB1, xMB2, xMB3, xMB4 = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )
  yMB1, yMB2, yMB3, yMB4 = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )

  wheels = [-2, -1, 0, 1, 2]
  stations = ['MB1', 'MB2', 'MB3', 'MB4']

  for w in wheels:
    avXMB1 = [i["eta"] for i in a if i["station"] == 1 and i["wheel"] == w ]
    avYMB1 = [i["rates"] for i in a if i["station"] == 1 and i["wheel"] == w ]
    xMB1.append( np.mean(avXMB1) )
    yMB1.append( np.mean(avYMB1) )

    avXMB2 = [i["eta"] for i in a if i["station"]   == 2 and i["wheel"] == w ]
    avYMB2 = [i["rates"] for i in a if i["station"] == 2 and i["wheel"] == w ]
    xMB2.append( np.mean(avXMB2) )
    yMB2.append( np.mean(avYMB2) )

    avXMB3 = [i["eta"] for i in a if i["station"]   == 3 and i["wheel"] == w ]
    avYMB3 = [i["rates"] for i in a if i["station"] == 3 and i["wheel"] == w ]
    xMB3.append( np.mean(avXMB3) )
    yMB3.append( np.mean(avYMB3) )

    avXMB4 = [i["eta"] for i in a if i["station"]   == 4 and i["wheel"] == w ]
    avYMB4 = [i["rates"] for i in a if i["station"] == 4 and i["wheel"] == w ]
    xMB4.append( np.mean(avXMB4) )
    yMB4.append( np.mean(avYMB4) )

  xlist = [xMB1, xMB2, xMB3, xMB4]
  ylist = [yMB1, yMB2, yMB3, yMB4]
  grList = []

  for s in stations:
#    plot_eta(xlist[stations.index(s)], ylist[stations.index(s)], s)
    grList.append(create_tgraphs(xlist[stations.index(s)], ylist[stations.index(s)], s))

  return grList
  #return grList[0], grList[1], grList[2], grList[3]

if __name__ == "__main__":
  main()





