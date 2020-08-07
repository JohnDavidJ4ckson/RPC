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
  #print "------ Creating Wheel TGraph ----------"
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

def create_plots(List, layer):
  H = 1600
  W = 800
  #print "----- Creating Third TCanvas -----"
  c = TCanvas("c", "Canvas",W,H)
  ymax = 0.0
  ymin = 100.0
  c.SetLeftMargin(0.15);
  c.SetRightMargin(0.06);
  c.SetTopMargin(0.09);
  c.SetBottomMargin(0.14);
  gPad.SetGrid()
  gPad.SetLogy()
  for gr in List:
    #print "The GR is ",gr.GetHistogram().GetMaximum()
    if ymax < gr.GetHistogram().GetMaximum():
      ymax = gr.GetHistogram().GetMaximum()
    if ymin > gr.GetHistogram().GetMinimum():
      ymin = gr.GetHistogram().GetMinimum()
    gr.SetMarkerColor(2)
  print "For "+layer+" the maximum is "+str(ymax)
  print "For "+layer+" the minimum is "+str(ymin)
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
  mg.SetTitle(layer)
  mg.GetXaxis().SetTitle( '#phi' )
  mg.GetYaxis().SetTitle( 'RPC/DT single hit rate ratio' )
  mg.SetMaximum( 50 ) #5*ymax)  # Acomodandolo a ojo 40)
  mg.SetMinimum( 0.9 ) #ymin/2)  # Acomodandolo a ojo 0.95)

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
  l.AddEntry(List[0], "RB1 / MB1", "p")
  l.AddEntry(List[1], "RB2 / MB2", "p")
  l.AddEntry(List[2], "RB3 / MB3", "p")
  l.AddEntry(List[3], "RB4 / MB4", "p")
  #l.SetTextSize(0.05)
  l.Draw("a");
  c.SaveAs("phiRatioDistro{}.png".format(layer))

## null -> dictionary
## The function uses the information about RPC and DT rates from
## other scripts and takes it as dictionaries. Then it produces
## a new dictionary with the ratio RPCrates/DTrates and the location
## of the station. The keys have the form W+2_L2_S01, and describe the
## wheel, layer, and station to which the ratio and phi location belong
def divide_rates():
  print "Retrieving RPC info"
  RPC = phiDistroRPC.main()
  print len(RPC)
  print RPC
  print "Retrieving DT info"
  DT  = generateDTTGraphs.main()
  print len(DT)

  ratioLayer1, ratioLayer2, ratioLayer3, ratioLayer4 = array('d'),array('d'),array('d'),array('d')
  ratioList = [ ratioLayer1, ratioLayer2, ratioLayer3, ratioLayer4 ]
  layers = [ 'L1', 'L2', 'L3', 'L4' ]
  ratioDict = {}
  for kDT,vDT in DT.items():
    for kRPC,vRPC in RPC.items():
      if (kDT[1:3] == kRPC[1:3]) and (kDT[5:7] == kRPC[5:7]) and (kDT[9:11] == kRPC[9:11]):
        name = kDT[:4]+layers[int(kDT[6]) - 1]+kDT[-4:]
        print name
        ratio = vRPC["rates"]/vDT["rates"]
        if ratio < 0.9: continue
        if ratio > 15: continue
        #print ratio
        indict = { "phi":vDT["phi"],
                   "ratio":ratio}
        ratioDict[name] = indict
  #print ratioDict
  return ratioDict

## dictionary -> dictionary
## This function takes the dictionary with the ratio and keys similar to 
## W+2_L3_S03. The chambers are used as the inputs of TGraphs. In the end 
## a new dictionary is returned with a TGraphs and with a key similar to W+2_RB3.
def generate_tgraphs(dict0):
  stations = ["L1", "L2", "L3", "L4"]
  wheels = ["-2", "-1", "+0", "+1", "+2"]
  chambers = [
             "01","02","03","04","05","06",
             "07","08","09","10","11","12"]
  grDict = {}
  for w in wheels:
    for s in stations:
    #Create lists to average here
      name = "W"+w+"_"+s
      xL1, xL2, xL3, xL4 = array('d'),array('d'),array('d'),array('d')
      yL1, yL2, yL3, yL4 = array('d'),array('d'),array('d'),array('d')
      xlist = [xL1, xL2, xL3, xL4]
      ylist = [yL1, yL2, yL3, yL4]
      for k,v in dict0.items():
        for c in chambers:
          if k == "W"+w+"_"+s+"_S"+c:
            stationIndex = stations.index(s)
            #print stationIndex
            xlist[stationIndex].append(v["phi"])
            ylist[stationIndex].append(v["ratio"])
      tgr  = create_tgraphs(xlist[stationIndex],ylist[stationIndex],name)
      #print name
      #print tgr       
      grDict[name] = tgr
  return grDict

def main():
  print "Retrieving Information"
  rDict = divide_rates()
  print "Producing the TGraph Dictionary"
  grDic = generate_tgraphs(rDict)
  print "Creating plots"
  wheels = ["W-2", "W-1", "W+0", "W+1", "W+2"]
  for w in wheels:
    tgraphList = [ grDic[k] for k,v in grDic.items() if w in k]
    create_plots(tgraphList, "Wheel"+w[-2]+w[-1])
  print "DONE"
  return

if __name__ == "__main__":
   main()

