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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def ratesEndcap_list():
  runNumfile = "output_rolls2018.json"
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
          if float(rates1["rate"][endcapSection+r+"_CH"+c+roll]["ratesquarecm"]) == 0: continue
          rates.append(float(rates1["rate"][endcapSection+r+"_CH"+c+roll]["ratesquarecm"]))
          names.append(endcapSection+r+"_CH"+c+roll)
        except KeyError:
          continue
  #print sorted(names)
  return [names, rates]

def ratesWheel_lists():
  runNumfile = "output_rolls2018.json"
  with open(runNumfile) as dataf:
    rates1 = json.loads(dataf.read())
  wheels = ["0", "1", "2"]
  rolls = ["1", "2", "3", "4"]
  subrolls = ["in","out","+","-", "++", "--"]
  chambers = [
             "01","02","03","04","05","06",
             "07","08","09","10","11","12"]
  ring = ["Forward", "Middle", "Backward"]
  parameters = ["W+"+w+"_"+wheelSection+s+"_S"+c+"_"+ri for w in wheels
                for s in subrolls for c in chambers for ri in ring
                if ( (w == "0") and (ri == "Forward") ) or ( w!="0" )]
  names = []
  rates = []
  for p in parameters:
    try:
      if float(rates1["rate"][p]["ratesquarecm"]) == 0: continue
      rates.append(float(rates1["rate"][p]["ratesquarecm"]))
      names.append(p)
    except KeyError:
      continue
  return [names, rates]

def etaWheel_lists():
  lines = []
  with open('W+Geometry.out', 'rw') as shakes:
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

def intersect_list(etaList, ratesList):
  intersect = set(etaList[0]).intersection(ratesList[0])
  print len(intersect)
  #newName  = []
  #newEta   = []
  #newRates = []
  dict0 = {}
  for i in intersect:
    etaIndex = etaList[0].index(i)
    rateIndex = ratesList[0].index(i)
    indict = { "eta": etaList[1][etaIndex],
               "rates":ratesList[1][rateIndex] }
    dict0[i] = indict
    #newName.append(i)
    #newEta.append(etaList[1][etaIndex])
    #newRates.append(ratesList[1][rateIndex])
  return dict0

def average_chambers(wheel, dictionary, X, Y):
  if wheel == 1:
    wheels = ["0", "1", "2"]
    rolls = ["1", "2", "3", "4"]
    subrolls = ["in","out","+","-", "++", "--"]
    chambers = [
               "01","02","03","04","05","06",
               "07","08","09","10","11","12"]
    ring = ["Forward", "Middle", "Backward"]
    for w in wheels:
      for s in subrolls:
        for ri in ring:
          eta = [v["eta"] for k, v in dictionary.items() 
                 for c in chambers if k == "W+"+w+"_"+wheelSection+s+"_S"+c+"_"+ri]
          rates = [v["rates"] for k, v in dictionary.items()
                 for c in chambers if k == "W+"+w+"_"+wheelSection+s+"_S"+c+"_"+ri]
          if rates and len(rates) != 1: 
            print max(set(rates), key=rates.count)
            X.append( max(set(eta), key=eta.count)     )
            Y.append( max(set(rates), key=rates.count) )
            #  X.append( median(eta)   )  #sum(eta)/len(eta) )
            #  Y.append( median(rates) )  #sum(rates)/len(rates) )

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
        eta = [v["eta"] for k, v in dictionary.items() for c in chambers if k == endcapSection+r+"_CH"+c+roll]
        rates = [v["rates"] for k, v in dictionary.items() for c in chambers if k == endcapSection+r+"_CH"+c+roll]
        if rates:# and len(rates) != 1:
          X.append( max(set(eta), key=eta.count)     )
          Y.append( max(set(rates), key=rates.count) )
          #  X.append( median(eta)   )  #sum(eta)/len(eta) )
          #  Y.append( median(rates) )  #sum(rates)/len(rates) )

def main():
  #if sys.argv[2]: print str(sys.argv[2])
  wheelEtaList = etaWheel_lists() #[names, eta] 
  print len(wheelEtaList[0]), len(wheelEtaList[1])
  endcapEtaList = etaEndcap_list() #[names, eta] 
  print len(endcapEtaList[0]), len(endcapEtaList[1])
  wheelRatesList = ratesWheel_lists() #[names, rates]
  print len(wheelRatesList[0]), len(wheelRatesList[1])
  endcapRatesList = ratesEndcap_list() #[names, rates]
  print len(endcapRatesList[0]), len(endcapRatesList[1])

  wheelIntersect = intersect_list(wheelEtaList,wheelRatesList) #name{eta, rates}
  endcapIntersect = intersect_list(endcapEtaList,endcapRatesList) #name{eta, rates}

  x, y = array( 'd' ), array( 'd' )

  average_chambers(1, wheelIntersect, x, y)
  average_chambers(0, endcapIntersect, x, y)

  print len(x)
  print len(y)

  return x, y

def eta_plot(X1,Y1,X2,Y2,X3,Y3,X4,Y4):
  n = len(X1+X2+X3+X4)
  listX = [X1, X2, X3, X4]
  listY = [Y1, Y2, Y3, Y4]

  print "----- Creating TGraph -----"
  X, Y = array( 'd' ), array( 'd' )

  for lx in listX:
    for i in range(len(lx)): X.append(lx[i])
    print len(lx)
  for ly in listY:
    for i in range(len(ly)): Y.append(ly[i])
    print len(ly)

  print len(X)
  print len(Y)
  H = 800
  W = 800
  canv = TCanvas("c1", "Canvas", W, H)

  n1 = len(X1)
  gr1 = TGraph(n1,X1,Y1)
  #gr = gr0.GetHistogram()
  gr1.SetLineColor( 2 )
  gr1.SetLineWidth( 4 )
  gr1.SetMarkerColor( kOrange )
  gr1.SetMarkerStyle( 21 )
  gr1.SetTitle( 'Layer 1' )
  gr1.GetXaxis().SetTitle( '#Eta' )
  gr1.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  #gr1.Draw("SAME AP")

  n2 = len(X2)
  gr2 = TGraph(n2,X2,Y2)
  #gr = gr0.GetHistogram()
  gr2.SetLineColor( 3 )
  gr2.SetLineWidth( 5 )
  gr2.SetMarkerColor( kBlue )
  gr2.SetMarkerStyle( 22 )
  gr2.SetTitle( 'Layer 2') 
  gr2.GetXaxis().SetTitle( '#Eta' )
  gr2.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  #gr2.Draw("SAME AP")

  n3 = len(X3)
  gr3 = TGraph(n3,X3,Y3)
  #gr = gr0.GetHistogram()
  gr3.SetLineColor( 4 )
  gr3.SetLineWidth( 6 )
  gr3.SetMarkerColor( kRed )
  gr3.SetMarkerStyle( 23 )
  gr3.SetTitle( 'Layer 3' )
  gr3.GetXaxis().SetTitle( '#Eta' )
  gr3.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  #gr3.Draw("SAME AP")

  n4 = len(X4)
  gr4 = TGraph(n4,X4,Y4)
  #gr = gr0.GetHistogram()
  gr4.SetLineColor( 5 )
  gr4.SetLineWidth( 7 )
  gr4.SetMarkerColor( kGreen )
  gr4.SetMarkerStyle( 24 )
  gr4.SetTitle( 'Layer 4' )
  gr4.GetXaxis().SetTitle( '#Eta' )
  gr4.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  #gr4.Draw("SAME")

  mg = TMultiGraph()
  mg.Add(gr1,"AP")
  mg.Add(gr2,"AP")
  mg.Add(gr3,"AP")
  mg.Add(gr4,"AP")
  mg.Draw("a")
  mg.SetTitle( 'Pseudorapidity Distribution')
  mg.GetXaxis().SetTitle( '#Eta' )
  mg.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )

  #legend = TLegend(0.1,0.7,0.48,0.9)
  #legend.SetHeader("The Legend Title","C") #// option "C" allows to center the header
  #legend.AddEntry("gr1","Function abs(#frac{sin(x)}{x})","l")
  #legend.AddEntry("gr2","Graph with error bars","lep")
  #legend.AddEntry("gr3","Graph with error bars","lep")
  #legend.AddEntry("gr4","Graph with error bars","lep")
  canv.BuildLegend(0.1,0.7,0.48,0.9)
  #legend.Draw()

  canv.SaveAs("etaDistro.gif")




if __name__ == "__main__":
  endcapSectionList = ["RE+1", "RE+2", "RE+3", "RE+4"]
  wheelSectionList  = ["RB1", "RB2", "RB3", "RB4"]
  endcapSection = "RE+4"
  wheelSection = "RB4"
  try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
  for opt, arg in opts:
      if opt == '-h':
          print 'test.py -i <inputfile> -o <outputfile>'
          sys.exit()
      elif opt in ("-i", "--ifile"):
          endcapSection = str(arg)
      elif opt in ("-o", "--ofile"):
          wheelSection = str(arg)
  x, y = [0,0,0,0], [0,0,0,0]
  for i in range(4):
    endcapSection = endcapSectionList[i]
    wheelSection = wheelSectionList[i]
    x[i],y[i] = main()

  eta_plot(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3])
  


