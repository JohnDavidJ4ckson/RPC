# -*- coding: utf-8 -*-
import json
import sys
from ROOT import *
from ROOT import gPad
import numpy as np 
from utils import load_json

class RPCMapCreator():
  
  def __init__( self ):
    print "mapcreator"
    self.rpc2Dmap = load_json("2DjsonMap.json") 
    #print self.rpc2Dmap

  def create2Dhistograms( self, data, maptype, dirAndName): 
    rpcmap = self.rpc2Dmap[maptype]
    hists = {}
    hmax = []
    hstd = []
    for k,v in rpcmap.iteritems():
      xlabels    = v["Xlabels"]
      ylabels    = v["Ylabels"]
      dimensions = v["BinsAndDimensions"]
      
      hname  = str(k)#+'_'+run#+'_'+HV
      htitle = str(k)#+', '+run 
      twoDimensionalHisto = TH2F(hname,htitle,dimensions[0],dimensions[1],dimensions[2],dimensions[3],dimensions[4],dimensions[5])
      
      for ii in range(len(xlabels)):
        twoDimensionalHisto.GetXaxis().SetBinLabel(ii+1,str(xlabels[ii]))
      for ii in range(len(ylabels)):
        twoDimensionalHisto.GetYaxis().SetBinLabel(ii+1,str(ylabels[ii]))

      coordinates = v["XYcoordinates"]
      for roll,xy in coordinates.iteritems():
        try:
          xx = xy[0]
          yy = xy[1]
          value = float(data[roll])
          twoDimensionalHisto.SetBinContent(xx,yy,value)
        except KeyError:
          continue
      
      twoDimensionalHisto.GetYaxis().SetTitle("Detector Unit")
      twoDimensionalHisto.GetXaxis().SetTitle("Sector")
      twoDimensionalHisto.GetYaxis().SetTitleSize(0.05)
      twoDimensionalHisto.GetYaxis().SetTitleOffset(0.96)
      twoDimensionalHisto.GetYaxis().SetTitleFont(42)
      #twoDimensionalHisto.GetZaxis().SetTitleSize(0.05)
      twoDimensionalHisto.GetZaxis().SetTitleFont(42)
      twoDimensionalHisto.GetZaxis().SetTitleOffset(0.7)
      twoDimensionalHisto.GetZaxis().SetTitle("rate")

      hmax.append(twoDimensionalHisto.GetMaximum())
      hstd.append(twoDimensionalHisto.GetStdDev())
      hists[str(k)] = twoDimensionalHisto


    median = np.median(hmax)
    stdevs = np.median(hstd)
    maxx    = median

    print median, stdevs, maxx

    for k,twoDimensionalHisto in hists.items():
      acan = TCanvas(k+"_can",k+"_can",1200,700)
      drawopt = "text COLZ"
      if "RE" in k:
        drawopt = "text89 COLZ"
      
      twoDimensionalHisto.SetStats(False)
      twoDimensionalHisto.SetMinimum(0.0)
      twoDimensionalHisto.SetMaximum(maxx)
      twoDimensionalHisto.Draw(drawopt)
      palette = twoDimensionalHisto.GetListOfFunctions().FindObject("palette")
      tex1 = TLatex(0.11,0.855,"CMS")
      tex1.SetNDC()
      tex1.SetTextFont(61)
      tex1.SetTextSize(0.06)
      tex1.SetLineWidth(2)
      
      tex2 = TLatex(0.11,0.805,"Preliminary");
      tex2.SetNDC();
      tex2.SetTextAlign(13);
      tex2.SetTextFont(52);
      tex2.SetTextSize(0.0456);
      tex2.SetLineWidth(2);
      acan.Update()
      nname = ""
      #nname = dirAndName
      if "+" in k:
        nname = dirAndName+"/"+k.replace("+","p")
      if "-" in k:
        nname = dirAndName+"/"+k.replace("-","m")
      acan.SaveAs(nname+"_2D"+".png")
   
    return hists
#  with open(ff) as data_file:
#    data = json.load(data_file)
#   return data
