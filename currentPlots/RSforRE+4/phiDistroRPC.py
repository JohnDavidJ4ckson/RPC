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
      curry = float(row[3])
      lummo = float(row[4])
      current.append(curry)
      lumi.append(lummo)
  #print current
  #print lumi

  return [current, lumi]

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

## list, string --> Nul
## The function receives a list with TGraphs for each RPC Layer
## and the name of a wheel. These are used to create a plot 
def plot_results(List, layer):
  H = 1600
  W = 800
  #print "----- Creating Third TCanvas -----"
  c = TCanvas("c", "Canvas",W,H)
  ymax = 0.0
  c.SetLeftMargin(0.15)
  c.SetRightMargin(0.06)
  c.SetTopMargin(0.09)
  c.SetBottomMargin(0.14)
  gPad.SetGrid()
  #gPad.SetLogy()
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
  List[1].SetMarkerColor( kGreen+3 )
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
  mg.GetXaxis().SetTitle( 'Instantaneous Luminosity (10^{30} cm^{-2} s^{-1})' )
  mg.GetYaxis().SetTitle( 'Current (#mu A)' )
  mg.SetMaximum(ymax+12)
  #mg.SetMinimum(-10.0)
  #mg.GetXaxis().SetLimits(0.,20000); 
  mg.GetXaxis().SetLabelFont(42)
  mg.GetXaxis().SetLabelOffset(0.007)
  mg.GetYaxis().CenterTitle(kTRUE)
  mg.GetXaxis().SetNdivisions(507)
  mg.GetXaxis().SetLabelSize(0.04)
  mg.GetXaxis().SetTitleSize(0.05)
  mg.GetXaxis().SetTitleOffset(1.2)
  mg.GetXaxis().SetTitleFont(42)
  mg.GetYaxis().SetLabelFont(42)
  mg.GetYaxis().SetLabelOffset(0.007)
  mg.GetYaxis().SetLabelSize(0.05)
  mg.GetYaxis().SetTitleSize(0.06)
  mg.GetYaxis().SetTitleOffset(1.2)
  mg.GetYaxis().SetTitleFont(42)

  pv = TPaveText(.08,0.93,.45,0.93,"NDC") 
  pv.AddText('CMS Preliminary')
  pv.SetFillStyle(0)
  pv.SetBorderSize(0)
  pv.SetTextSize(0.03)
  pv.Draw()
  pv1 = TPaveText(.55,0.93,.9,0.93,"NDC")

  chamber1 = 'CH'+layer[7:9]
  chamber2 = 'CH'+layer[9:11]
  chamber3 = 'CH'+layer[11:13]

  pv1.AddText('RE+4, '+chamber1+', '+chamber2+', '+chamber3+' (13 TeV)')
  pv1.SetFillStyle(0)
  pv1.SetBorderSize(0)
  pv1.SetTextSize(0.03)
  pv1.Draw()

  fun1 = TF1("fun1","pol1",7000,19000)
  fun2 = TF1("fun2","pol1",9000,19000)

  fit1 = List[0].Fit("fun1","FQR") # "FQ")
  fit2 = List[1].Fit("fun2","FQR") # "FQ")

  offset1 = fun1.GetParameter(0)
  offset2 = fun2.GetParameter(0)
  slope1 = fun1.GetParameter(1)
  slope2 = fun2.GetParameter(1)
  slopeRatio = slope2/slope1

  l = TLegend(0.18,0.75,0.75,0.88)
  l.SetFillColor(0)
  l.SetBorderSize(1)
  l.SetTextSize(0.022)
  l.SetNColumns(1)
  l.SetMargin(.05)
  #l.SetTextAlign(13)
  l.SetHeader("The data is fit to a line: Current = m #times Ins. Luminosity + b","C")
  l.AddEntry(List[0], "fill 7080 (before TS2) The offset is {0:.{1}f}".format(offset1,2) + " and the slope is {0:.{1}f}".format(slope1,4), "p")
  l.AddEntry(List[1], "fill 7252 (after TS2) The offset is {0:.{1}f}".format(offset2,2)  + " and the slope is {0:.{1}f}".format(slope2,4), "p")
  l.AddEntry( None, "The ratio of slopes  m(7252)/m(7080) is {0:.{1}f}".format(slopeRatio,6) , "")
  l.Draw("")

  c.SaveAs("currentDistroRPC_{}.png".format(layer))
  return slopeRatio

## Null -> Null
## The main function uses the rest of functions to create a TGraph dictionary
## in the agreed granularity then distribute it to the plotting function.
def plot_ts2_comparison(sector):
  print "outputs/lumisection_afterTS2{}.csv".format(sector) 
  return
  print "Retrieving rates Info"
  print "Loading Files' Data"
  listaRatesAfterTS2CH =  rates_endcap_list("outputs/lumisection_afterTS2{}.csv".format(sector))
  listaRatesBeforeTS2CH = rates_endcap_list("outputs/lumisection_beforeTS2{}.csv".format(sector))
  print "Generating TGraphs"
  print "THIS is AFTER"
  tgraphsDictionaryAfterTS2  = generate_tgraphs(listaRatesAfterTS2CH,'RE-4 after TS2')
  print "THIS is BEFORE"
  tgraphsDictionaryBeforeTS2 = generate_tgraphs(listaRatesBeforeTS2CH,'RE-4 before TS2')
  print "Creating plots"
  tgraphList = [ tgraphsDictionaryBeforeTS2, tgraphsDictionaryAfterTS2 ]
  slopeRatio = plot_results(tgraphList, "RE+4_CH{}_TS2".format(sector[2:]))
  print "DONE"
  return slopeRatio

def main():
  chamberNumbers = ["{0:02d}".format(i+1)  for i in range(36)]
  #print chamberNumbers

  fileNames = []
  for i in range(36):
    n0 = (i-1) % 36
    n1 = (i) % 36
    n2 = (i+1) % 36
    string = 'ch'+chamberNumbers[n0]+chamberNumbers[n1]+chamberNumbers[n2]
    if i%3 == 0: fileNames.append(string)
  #print fileNames
  slopeRatio = []
  for f in fileNames:
    ratio = plot_ts2_comparison(f)
    slopeRatio.append(ratio)
  print fileNames
  print slopeRatio

if __name__ == "__main__":
  main()

