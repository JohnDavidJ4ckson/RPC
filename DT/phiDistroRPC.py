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

## Value -> Boolean
## This function returns True if the given object is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

## Null ->  List of lists [string, double]
## The function uses a fixed txt file with the geometric information
## of the RPC's in the barrel and returns a list of names and their
## corresponding pseudorapidity mean location.
def phiWheel_lists_RPC():
  lines = []
  with open('GeometryWheelRPC.out', 'rw') as shakes:
    for line in shakes:
      y = line.split(" glob(X,Y,Z)")
      lines.append(y)
  name = []
  phi = []
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
    phi1 = v1.Phi()
    # Informacion del last strip
    maxEtaList0 = line[2].split("(")
    maxEtaList1 = maxEtaList0[1].split(",")   # Las entradas 0 y 1 son las coordenadas X y Y del strip
    maxEtaList2 = maxEtaList1[2].split(r")")  # La entrada 0 de esta lista es la coordenada Z del strip
    maxX = float(maxEtaList1[0])
    maxY = float(maxEtaList1[1])
    maxZ = float(maxEtaList2[0])
    v2 = TVector3(minX,minY,minZ)
    phi2 = v2.Phi()
    avgPhiValue = ( phi1 + phi2 ) /2
    phiDegrees = avgPhiValue * (180/3.14159265359)
    if phiDegrees < -10.0: phiDegrees = 360+phiDegrees
    elif phiDegrees == 4.900302002323386: phiDegrees = 180+4.900302002323386
    phi.append(phiDegrees)
  List = [name, phi]
  return List

## Null -> List of lists [string, double]
## The function uses a fixed json file to return a list of lists with 
## RPC Id names in the first entry and the corresponding rates in 
## the second entry. The IDnames are createad as they would correspond
## to RPC in the Barrel section.
def ratesWheel_lists_RPC():
  runNumfile = "ratesAt1p5.json" #"output_rolls2018.json"
  with open(runNumfile) as dataf:
    rates1 = json.loads(dataf.read())
  wheels = ["0", "1", "2"]
  rolls = ["1", "2", "3", "4"]
  subrolls = ["","+","-","in","out", "++", "--"]
  chambers = [
             "01","02","03","04","05","06",
             "07","08","09","10","11","12"] # faltan 4, 9, 11
  ring = ["Forward", "Middle", "Backward"]
  wheelSectionList  = ["RB1", "RB2", "RB3", "RB4"]
  wheelSectionList0 = ["-","+"]
  parameters = ["W"+wS0+w+"_"+wS+s+"_S"+c+"_"+ri for w in wheels
                for s in subrolls for c in chambers for ri in ring for wS0 in wheelSectionList0
                for wS in wheelSectionList]
                #if ( (w == "0") and (ri == "Forward") ) or ( w!="0" )]
  #W+2_RB2out_S10_Middle
  names = []
  rates = []
  for p in parameters:
    try:
      if float(rates1[p]) == 0 or isnan(float(rates1[p])): continue
      rates.append(float(rates1[p]))
      names.append(p)
    except KeyError:
      continue
  List = [names, rates]
  return List

## List of lists [string, double], 
## List of lists [string, double]  -> Dictionary
## The function maps the rates and pseudorapidities that share ID 
## names to each other and returns them in a dictionary
def the_list(phiList, ratesList):
  intersect = set(phiList[0]).intersection(ratesList[0])
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
  gr.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  return gr

## null -> List[four tgraphs]
## The main function takes the list of dictionaries
## that has the information about eta, rates, and the
## geometry of the DT detector. Then it avarages over
## the wheels and produces the TGraphs that are exported
## for the etaDistro.py that compares them with RPC data.
def main(): # 1 for eta, 2 for phi
  phiList = phiWheel_lists_RPC()
  ratesList  = ratesWheel_lists_RPC()
  dictionary = the_list(phiList,ratesList)
  xRB1, xRB2, xRB3, xRB4 = array('d'),array('d'),array('d'),array('d')
  yRB1, yRB2, yRB3, yRB4 = array('d'),array('d'),array('d'),array('d')
  xlist = [xRB1, xRB2, xRB3, xRB4]
  ylist = [yRB1, yRB2, yRB3, yRB4]
  stations = ["RB1","RB2","RB3", "RB4"]
  wheels = ["0", "1", "2", "1", "2"]
  rolls = ["1", "2", "3", "4"]
  subrolls = ["","+","-","in","out", "++", "--"]
  chambers = [
             "01","02","03","04","05","06",
             "07","08","09","10","11","12"] # faltan 4, 9, 11
  ring = ["Forward", "Middle", "Backward"]
  wheelSectionList  = ["RB1", "RB2", "RB3", "RB4"]
  wheelSectionList0 = ["-","+"]
  parameters = ["W"+wS0+w+"_"+wS+s+"_S"+c+"_"+ri for w in wheels
                for s in subrolls for c in chambers for ri in ring for wS0 in wheelSectionList0
                for wS in wheelSectionList]

  for wS in wheelSectionList:
    for c in chambers:
      phi = [float( v["phi"] ) for k, v in dictionary.items() if not isnan(v["phi"]) 
           for w in wheels for ri in ring for wS0 in wheelSectionList0 for s in subrolls
           if k == "W"+wS0+w+"_"+wS+s+"_S"+c+"_"+ri]
      rates = [float( v["rates"] ) for k, v in dictionary.items() if not isnan(v["rates"]) 
           for w in wheels for ri in ring for wS0 in wheelSectionList0 for s in subrolls
           if k == "W"+wS0+w+"_"+wS+s+"_S"+c+"_"+ri]
      if rates:
        #print names
        #print eta
        #print median(eta)
        xlist[wheelSectionList.index(wS)].append( median(phi)   )  #sum(eta)/len(eta) )
        ylist[wheelSectionList.index(wS)].append( median(rates) )  #sum(rates)/len(rates) ) 
  #xRB1 = np.multiply( xRB1, (180/3.14159265359) )
  grList = []
  #grList.append( create_tgraphs(xRB1, yRB1, "RB1in") )
  
  for s in stations:
    grList.append( create_tgraphs(xlist[stations.index(s)],ylist[stations.index(s)],s) )

  print grList
  #return grList
  return xlist, ylist
if __name__ == "__main__":
  List = main()

#
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
    #gr.SetMaximum(300)
    #gr.Draw("p same hist")
    #gr.SetStats(0)

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
  mg.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  mg.SetMaximum(100)
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
  l = TLegend(0.25,0.80,0.75,0.85)
  l.SetFillColor(0)
  l.SetBorderSize(0)
  l.SetTextSize(0.03)
  l.SetNColumns(4)
  l.AddEntry(List[0], "MR1", "p")
  l.AddEntry(List[1], "MR2", "p")
  l.AddEntry(List[2], "MR3", "p")
  l.AddEntry(List[3], "MR4", "p")
  #l.SetTextSize(0.05)
  l.Draw("a");

  c.SaveAs("phiDistroRPC.png")
