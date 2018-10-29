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
#import CMS_lumi, tdrstyle
#import RPCRates
from numpy import isnan
import currentVsLumiPlots

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

## list, string --> Nul
## The function receives a list with TGraphs for each RPC Layer
## and the name of a wheel. These are used to create a plot 
def plot_results(List, layer, wheel, rb):
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
  #gPad.SetLogy()
  if ymax < max(List.GetY()):
    ymax = max(List.GetY())
  #for gr in List:
  #  if ymax < max(gr.GetY()):
  #    ymax = max(gr.GetY())
    #gr.SetMarkerColor(2)
    #print "The TGraph has this number of elements"
    #print gr.GetN()
    #gr.SetMaximum(300)
    #gr.Draw("p same hist")
    #gr.SetStats(0)

  #print " ------------ Creating TMultiGraph -----------"
  List.SetMarkerColor( kRed )
  #List[0].SetMarkerStyle( 21 )
  #List[1].SetMarkerColor( kRed+2 )
  #List[1].SetMarkerStyle( 22 )
  #List[2].SetMarkerColor( kBlue )
  #List[3].SetMarkerStyle( 23 )
  #List[3].SetMarkerColor( kBlue+2 )
  List.SetMarkerStyle(8)
  #List[1].SetMarkerStyle(20)
  #List[2].SetMarkerStyle(25)
  #List[3].SetMarkerStyle(23)

  #maxY = 12
  mg = TMultiGraph()
  mg.Add(List,"AP")
  #mg.Add(List[1],"AP")
  #mg.Add(List[2],"AP")
  #mg.Add(List[3],"AP")
  mg.Draw("a")
  mg.SetTitle( "")
  mg.GetXaxis().SetTitle( '#phi' )
  mg.GetYaxis().SetTitle( '{} Ratio'.format(layer) )
  mg.SetMaximum(ymax+.2)
  if layer == "slopes": mg.SetMaximum(ymax+.04)
  mg.GetXaxis().SetLabelFont(42)
  mg.GetXaxis().SetLabelOffset(0.007)
  mg.GetXaxis().SetLabelSize(0.043)
  mg.GetXaxis().SetTitleSize(0.05)
  mg.GetXaxis().SetTitleOffset(1.06)
  mg.GetXaxis().SetTitleFont(42)
  mg.GetYaxis().SetLabelFont(42)
  mg.GetYaxis().SetLabelOffset(0.008)
  mg.GetYaxis().SetLabelSize(0.04)
  mg.GetYaxis().SetTitleSize(0.04)
  mg.GetYaxis().SetTitleOffset(1.5)
  mg.GetYaxis().SetTitleFont(42)

  pv = TPaveText(.08,0.93,.45,0.93,"NDC") 
  pv.AddText('CMS Preliminary')
  pv.SetFillStyle(0)
  pv.SetBorderSize(0)
  pv.SetTextSize(0.03)
  pv.Draw()

  pv1 = TPaveText(.7,0.93,.9,0.93,"NDC")
  pv1.AddText(wheel+', '+rb+', (13 TeV)')
  pv1.SetFillStyle(0)
  pv1.SetBorderSize(0)
  pv1.SetTextSize(0.03)
  pv1.Draw()
  l = TLegend(0.25,0.78,0.75,0.88)
  l.SetFillColor(0)
  l.SetBorderSize(0)
  l.SetTextSize(0.022)
  l.SetNColumns(1)
  l.AddEntry(List, "Ratio of the {} from linear fits to fill(7252) / fill(7080) data".format(layer), "p")
  #l.AddEntry(List[1], "RE+4 run 323471 (after TS2)", "p")
  #l.AddEntry(List[2], "RE-4 run 322355 (before TS2)", "p")
  #l.AddEntry(List[3], "RE+4 run 322355 (before TS2)", "p")
  #l.SetTextSize(0.05)
  l.Draw("a");

  c.SaveAs("phiDistroRPC_{}_{}_{}.png".format(layer,wheel,rb))

## Null -> Null
## The main function uses the rest of functions to create a TGraph dictionary
## in the agreed granularity then distribute it to the plotting function.
def main(wheel, rb):
  #print "Retrieving rates Info"
  #listaRatesAfterTS2 =  rates_endcap_list("run323471/output_rolls.json")
  #listaRatesBeforeTS2 = rates_endcap_list("run322355/output_rolls.json")
  #print "Retrieving rates Info"
  #listaPhi = phi_endcap_list()
  phi = [(i)*30 for i in range(12)]
  filenames, slopeRatio, offsetRatio = currentVsLumiPlots.main(wheel,rb)
  phiArray         = array('d') #np.array(phi)
  slopeRatioArray  = array('d') #np.array(slopeRatio)
  offsetRatioArray = array('d') #np.array(offsetRatio)
  for p in phi: phiArray.append(p)
  for s in slopeRatio: slopeRatioArray.append(s)
  for o in offsetRatio: offsetRatioArray.append(o)

  slopeTG  = create_tgraphs(phiArray,slopeRatioArray,"slopes")
  offsetTG = create_tgraphs(phiArray,offsetRatioArray,"offset")
  plot_results(slopeTG, "slopes", wheel, rb)
  plot_results(offsetTG, "offset",wheel, rb)
  return

if __name__ == "__main__":
  wheels = ['W+2', 'W+1', 'W-1', 'W-2'] #W+0
  RBs = ['RB1', 'RB2', 'allRB'] #RB4, RB3
  for w in wheels:
    for rb in RBs:
      main(w, rb)

