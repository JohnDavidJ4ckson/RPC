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

def rates_list():
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
          if float(rates1["rate"]["RE+4"+r+"_CH"+c+roll]["ratesquarecm"]) == 0: continue
          rates.append(float(rates1["rate"]["RE+4"+r+"_CH"+c+roll]["ratesquarecm"]))
          names.append("RE+4"+r+"_CH"+c+roll)
        except KeyError:
          continue

 # print len(names)
 # print len(rates)
  return [names, rates]

def main():
  
  lines = []
  with open('file.out', 'rw') as shakes:
    for line in shakes:
      #lines.append(line.rstrip('\n'))
      y = line.split(",")
      lines.append(y)
      #line.replace("(.*)glob(.*)","(.*)globes(.*)")
  
  #print lines[1]
  
  name = []
  etaMin = []
  etaMax = []
  etaAvg = []
  for line in lines:
    #print line[0], line[3], line[4]
  
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
    #print minEtaValue
  
  #print len(etaMin)
  #print len(etaMax)
  #print len (name)
  #print len(etaAvg)
  #
  theList = [name, etaAvg]
  #print theList
  #print len(theList)
  
  theRatesList = rates_list() #[names, rates]
  
  
  Intersect = set(theList[0]).intersection(theRatesList[0])
  #print len(Intersect)
  
  distroX = [] # Eta
  distroY = [] # RateSqm
  #print "---- Creating arrays to fill TGraph ----"
  x, y = array( 'd' ), array( 'd' )
  #print "----- Arrays have been created -------"

  hpxpy = TH2F( 'hpxpy', 'hpxpy', 40, 1, 2, 40, 0, 30 )
  
  for i in Intersect:
    etaIndex = theList[0].index(i)
    rateIndex = theRatesList[0].index(i)
  
    #print etaIndex
    #print rateIndex    
  
    x.append(theList[1][etaIndex])
    y.append(theRatesList[1][rateIndex])
    
    hpxpy.Fill( theList[1][etaIndex], theRatesList[1][rateIndex] )

  print "----- Printing Arrays of interest ------"
  #print x
  #print y
  
  n = 210
  print "----- Creating TGraph -----"
  gr = TGraph(n,x,y)
  #gr = gr0.GetHistogram()
  gr.SetLineColor( 2 )
  gr.SetLineWidth( 4 )
  gr.SetMarkerColor( 4 )
  gr.SetMarkerStyle( 21 )
  gr.SetTitle( 'Pseudorapidity Distribution for RE+4' )
  gr.GetXaxis().SetTitle( '#Eta' )
  gr.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )


  H = 1600
  W = 800
  canv = TCanvas("c1", "Canvas", W, H)
  gr.Draw("AP")
  canv.SaveAs("TestingTGraph.gif")

  hpxpy.SetLineColor( 2 )
  hpxpy.SetLineWidth( 4 )
  hpxpy.SetMarkerColor( 4 )
  hpxpy.SetMarkerStyle( 21 )
  hpxpy.SetTitle( 'Pseudorapidity Distribution for RE+4' )
  hpxpy.GetXaxis().SetTitle( '#Eta' )
  hpxpy.GetYaxis().SetTitle( 'RPC single hit rate (Hz/cm^{2})' )
  
  hpxpy.Draw("P")
  canv.SaveAs("TestingTH2D.gif")
  
  # Looping over file to fill Endcap bins
  #for element in lines:
  #  print(element)
  #print(lines[0].find("e", 12, 19))
  
  #enumerate(lines)
  ##print(list(enumerate(lines)))
  #
  #pattern = re.compile(r"\be\w*a\b", re.IGNORECASE)
  #
  ####################################
  ########### Este patrn acomoda las columnas de Endcap
  #### grep -v W  RPCGeometry.out | grep RE | sed 's/\[cm\][^)]*RE/[cm]\n RE/g' | sed 's/.*RE/RE/' 
  ###########
  ##### Y con este comando se creo file.out
  #### grep -v W  RPCGeometry.out | grep RE | sed 's/\[cm\][^)]*RE/[cm]\n RE/g' | sed 's/.*RE/RE/' | awk 'NR%4==0' > file.out
  ####################################
  #
  #
  #substr = "eta"
  #
  #for linenum, line in enumerate(lines):
  #  print(linenum, line)
  #  index = 0               # Set the search index to the first character,
  #  string = lines[linenum]
  #  if pattern.search(string) != None:
  #    print("Found it!")
  #
  #  while index < len(string): #While index is a number smaller than the number of letters in str.
  #    index = string.find(substr, index) #set index to location of first remaining occurrence of "e"
  #    if index == -1:         # If nothing was found,
  #      break            # exit the while loop. Otherwise,
  #    print("Line: ", linenum, "Index: ", index) # Print the linenum and index of the located substr.
  #    index += len(substr)    # Before repeating search, increment index by length of substr. 


if __name__ == "__main__":
  test = main()
