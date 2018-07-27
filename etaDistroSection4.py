#!/usr/bin/env python

import re
import json
import sys
from ROOT import *
from ROOT import gPad
from ROOT import TCanvas, TGraph
from ROOT import gROOT
from array import array

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
  rolls = ["_A","_B","_C"]
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
          if float(rates1["rate"]["RE+4"+r+"_CH28"+roll]["ratesquarecm"]) == 0: continue
          rates.append(float(rates1["rate"]["RE+4"+r+"_CH28"+roll]["ratesquarecm"]))
          names.append("RE+4"+r+"_CH28"+roll)
        except KeyError:
          continue

 # print len(names)
 # print len(rates)
  return [names, rates]

def ratesWheel_list():
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
  parameters = ["W+"+w+"_RB4"+s+"_S10"+"_"+ri for w in wheels
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
      #lines.append(line.rstrip('\n'))
      y = line.split(",")
      lines.append(y)
      #line.replace("(.*)glob(.*)","(.*)globes(.*)")

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
                 for c in chambers if k == "W+"+w+"_RB4"+s+"_S10"+"_"+ri]
          rates = [v["rates"] for k, v in dictionary.items()
                 for c in chambers if k == "W+"+w+"_RB4"+s+"_S10"+"_"+ri]
          names = [k for k, v in dictionary.items()
                 for c in chambers if k == "W+"+w+"_RB4"+s+"_S10"+"_"+ri]

          if rates and len(rates) != 1: 
            X.append( sum(eta)/len(eta) )
            Y.append( sum(rates)/len(rates) )
          print names
  elif wheel == 0:
    rolls = ["_A","_B","_C"]
    chambers = [
               "01","02","03","04","05","06","07","08","09",
          "10","11","12","13","14","15","16","17","18","19",
          "20","21","22","23","24","25","26","27","28","29",
          "30","31","32","33","34","35","36"
          ]
    ring = ["_R2", "_R3"]
    for r in ring:
      for roll in rolls:
        eta = [v["eta"] for k, v in dictionary.items() for c in chambers if k == "RE+4"+r+"_CH28"+roll]
        rates = [v["rates"] for k, v in dictionary.items() for c in chambers if k == "RE+4"+r+"_CH28"+roll]
        names = [k for k, v in dictionary.items() for c in chambers if k == "RE+4"+r+"_CH28"+roll]
        if rates:# and len(rates) != 1:       
          X.append( sum(eta)/len(eta) )
          Y.append( sum(rates)/len(rates) )
        #print names
   
def main():
  wheelEtaList = etaWheel_lists() #[names, eta] 
  print len(wheelEtaList[0]), len(wheelEtaList[1])
  endcapEtaList = etaEndcap_list() #[names, eta] 
  print len(endcapEtaList[0]), len(endcapEtaList[1])
  wheelRatesList = ratesWheel_list() #[names, rates]
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

  n = len(x)
  print "----- Creating TGraph -----"
  gr = TGraph(n,x,y)
  #gr = gr0.GetHistogram()
  gr.SetLineColor( 2 )
  gr.SetLineWidth( 4 )
  gr.SetMarkerColor( 4 )
  gr.SetMarkerStyle( 21 )
  gr.SetTitle( 'Pseudorapidity Distribution for Layer 4' )
  gr.GetXaxis().SetTitle( '#Eta' )
  gr.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  H = 800
  W = 800
  canv = TCanvas("c1", "Canvas", W, H)
  gr.Draw("AP")
  canv.SaveAs("etaDistro.gif")
  canv.SaveAs("etaDistro.pdf")
  canv.SaveAs("etaDistro.png")


if __name__ == "__main__":
  test = main()

