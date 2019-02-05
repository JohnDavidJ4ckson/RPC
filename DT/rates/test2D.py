import os, json
from optparse import OptionParser
from RPCRates import *
from RPCmapCreator import RPCMapCreator 
from ROOT import * #TFile, TGraph, TMultiGraph, TLegend, TCanvas, TAxis, gStyle, TLatex, TH1D
import math

def main():  
  #rpcrate = RPCRates('320688',"m")
  rpcrate = RPCRates('306421',"m")
  #d = rpcrate.barrel2Dmap()
  #print d
  mapcreator = RPCMapCreator()
  mapcreator.create2Dhistograms( rpcrate.barrel2Dmap(), 'forDT')

if __name__ == "__main__":
  test = main()
