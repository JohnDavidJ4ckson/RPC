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

#eta = ["eta min =", "eta max ="]
# 
# with open("RPCGeometry.out", "r") as shakes, open('newfile.txt', 'w') as newfile:
#     for line in shakes:
#         if any(bad_word in line for bad_word in eta):
#             newfile.write(line)

def rates_lists():
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
  parameters = ["W+"+w+"_RB4"+s+"_S"+c+"_"+ri for w in wheels
                for s in subrolls for c in chambers for ri in ring
                if ( (w == "0") and (ri == "Forward") ) or ( w!="0" )]
  names = []
  rates = []

  for p in parameters:
    try:
      if  float(rates1["rate"][p]["ratesquarecm"]) == 0: continue
      rates.append(float(rates1["rate"][p]["ratesquarecm"]))
      names.append(p)
    except KeyError:
      continue

  return [names, rates]

def eta_list():
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

def azimutalAverage():
  wheels = ["0", "1", "2"]
  rolls = ["1", "2", "3", "4"]
  subrolls = ["in","out","+","-", "++", "--"]
  chambers = [
             "01","02","03","04","05","06",
             "07","08","09","10","11","12"]
  ring = ["Forward", "Middle", "Backward"]
  parameters = ["W+"+w+"_RB4"+s+"_S"+c+"_"+ri for w in wheels
                for s in subrolls for c in chambers for ri in ring
                if ( (w == "0") and (ri == "Forward") ) or ( w!="0" )]
  names = []
  rates = []

  for p in parameters:
    try:
      if  float(rates1["rate"][p]["ratesquarecm"]) == 0: continue
      rates.append(float(rates1["rate"][p]["ratesquarecm"]))
      names.append(p)
    except KeyError:
      continue

  return [names, rates]
  

def main():
  theList = eta_list() #[names, eta] 
  print len(theList[0]), len(theList[1])
  print len(theList)
  
  theRatesList = rates_lists() #[names, rates]
  print len(theRatesList[0])
  print len(theRatesList[1])

##########################################################
##### Aqui va el loop para promediar en la parte azimutal
##########################################################
  for i in range(len(theList[0])):
    try:
      print theList[0][i]
      if theList[0][i][9] == "S":# o 10]:
         index = theList[1].index(theList[1][i])
         del theList[0][index]
         del theList[1][index]
    except IndexError:
      continue
##########################################################
##########################################################

  Intersect = set(theList[0]).intersection(theRatesList[0])
  print len(Intersect)
  
  distroX = [] # Eta
  distroY = [] # RateSqm
  print "---- Creating arrays to fill TGraph ----"
  x, y = array( 'd' ), array( 'd' )
  print "----- Arrays have been created -------"

#  hpxpy = TH2F( 'hpxpy', 'hpxpy', 40, 1, 2, 40, 0, 30 )
  
  for i in Intersect:
    etaIndex = theList[0].index(i)
    rateIndex = theRatesList[0].index(i)
  
    #print etaIndex
    #print rateIndex    
 
    x.append(theList[1][etaIndex])
    y.append(theRatesList[1][rateIndex])
    
#    hpxpy.Fill( theList[1][etaIndex], theRatesList[1][rateIndex] )
 
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
  gr.SetTitle( 'Pseudorapidity Distribution for W+' )
  gr.GetXaxis().SetTitle( '#Eta' )
  gr.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )


  H = 800
  W = 800
  canv = TCanvas("c1", "Canvas", W, H)
  gr.Draw("AP")
  canv.SaveAs("TestingTGraphWheel.gif")

#  hpxpy.SetLineColor( 2 )
#  hpxpy.SetLineWidth( 4 )
#  hpxpy.SetMarkerColor( 4 )
#  hpxpy.SetMarkerStyle( 21 )
#  hpxpy.SetTitle( 'Pseudorapidity Distribution for RE+4' )
#  hpxpy.GetXaxis().SetTitle( '#Eta' )
#  hpxpy.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  
#  hpxpy.Draw("P")
#  canv.SaveAs("TestingTH2D.gif")
#  
#  # Looping over file to fill Endcap bins
#  #for element in lines:
#  #  print(element)
#  #print(lines[0].find("e", 12, 19))
#  
#  #enumerate(lines)
#  ##print(list(enumerate(lines)))
#  #
#  #pattern = re.compile(r"\be\w*a\b", re.IGNORECASE)
#  #
#  ####################################
#  ########### Este patrn acomoda las columnas de Endcap
#  #### grep -v W  RPCGeometry.out | grep RE | sed 's/\[cm\][^)]*RE/[cm]\n RE/g' | sed 's/.*RE/RE/' 
#  ###########
#  ##### Y con este comando se creo file.out
#  #### grep -v W  RPCGeometry.out | grep RE | sed 's/\[cm\][^)]*RE/[cm]\n RE/g' | sed 's/.*RE/RE/' | awk 'NR%4==0' > file.out
#  ####################################
#  #
#  #
#  #substr = "eta"
#  #
#  #for linenum, line in enumerate(lines):
#  #  print(linenum, line)
#  #  index = 0               # Set the search index to the first character,
#  #  string = lines[linenum]
#  #  if pattern.search(string) != None:
#  #    print("Found it!")
#  #
#  #  while index < len(string): #While index is a number smaller than the number of letters in str.
#  #    index = string.find(substr, index) #set index to location of first remaining occurrence of "e"
#  #    if index == -1:         # If nothing was found,
#  #      break            # exit the while loop. Otherwise,
#  #    print("Line: ", linenum, "Index: ", index) # Print the linenum and index of the located substr.
#  #    index += len(substr)    # Before repeating search, increment index by length of substr. 
#

if __name__ == "__main__":
  test = main()
