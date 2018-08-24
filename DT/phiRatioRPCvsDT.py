#!/usr/bin/env python
import re
#import json
import sys
import getopt
from ROOT import *
from ROOT import gPad
from ROOT import TCanvas, TGraph
from ROOT import gROOT
from array import array
from numpy import median
import numpy as np
#from scipy import stats
import ROOT as rt
import CMS_lumi, tdrstyle
#import RPCRates
#from numpy import isnan
import phiDistroRPC
import generateDTTGraphs

## array, array, string -> TGraph
## The function recieves an x and y values to create
## a tgraph of them with the given name.
## This function is imported for use in the etaDistro.py file
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
  gr.GetXaxis().SetTitle( '#phi' )
  gr.GetYaxis().SetTitle( 'RPC/DT single hit rate (Hz/cm^{2})' )
  return gr

def main():
  phiRPC, ratesRPC = phiDistroRPC.main()
  phiDT,  ratesDT  = generateDTTGraphs.main(0)
  ratioLayer1, ratioLayer2, ratioLayer3, ratioLayer4 = array('d'),array('d'),array('d'),array('d')
  ratioList = [ ratioLayer1, ratioLayer2, ratioLayer3, ratioLayer4 ]
  layers = [ 'Layer 1', 'Layer 2', 'Layer 3', 'Layer 4' ]
  for i in ratioList:
    index = ratioList.index(i)
    for n in range(len(ratesRPC[index])):
      i.append( ratesRPC[index][n] / ratesDT[index][n] )
  grList = [ create_tgraphs( phiRPC[i], ratioList[i], 'Layer{}'.format(i+1) ) for i in range(len(ratioList)) ]
  return grList

if __name__ == "__main__":
  List = main()
  print List
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
    if ymax < gr.GetMaximum():
      ymax = gr.GetMaximum()
    gr.SetMarkerColor(2)

  #print " ------------ Creating TMultiGraph -----------"
  #List[0].SetMarkerColor( kRed+2 )
  #List[0].SetMarkerStyle( 21 )
  #List[1].SetMarkerColor( kBlue+2 )
  #List[1].SetMarkerStyle( 22 )
  #List[2].SetMarkerColor( kMagenta+2 )
  #List[3].SetMarkerStyle( 23 )
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
  mg.SetTitle( 'All Wheels')
  mg.GetXaxis().SetTitle( '#phi' )
  mg.GetYaxis().SetTitle( 'RPC/DT single hit rate (Hz/cm^{2})' )
  mg.SetMaximum(50)

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
  l = TLegend(0.25,0.75,0.75,0.85)
  l.SetFillColor(0)
  l.SetBorderSize(0)
  l.SetTextSize(0.03)
  l.SetNColumns(2)
  l.AddEntry(List[0], "RB1 / MR1", "p")
  l.AddEntry(List[1], "RB2 / MR2", "p")
  l.AddEntry(List[2], "RB3 / MR3", "p")
  l.AddEntry(List[3], "RB4 / MR4", "p")
  #l.SetTextSize(0.05)
  l.Draw("a");
  c.SaveAs("phiRatioDistro.png")



