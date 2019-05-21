import os
from optparse import OptionParser
from RPCRates import *
import math
from RPCmapCreator import RPCMapCreator 
from utils import load_json, fillgraphs, printmultigraph, fitGraph
from ROOT import TH1D, TCanvas, kBlue, kRed, TLegend, kBlack, kGreen
import numpy as np

def hsettings( g ):
  g.SetStats(0)
  g.GetXaxis().SetTitle("#phi")
  g.GetXaxis().SetLabelFont(42)
  g.GetXaxis().SetLabelOffset(0.007)
  g.GetXaxis().SetLabelSize(0.043)
  g.GetXaxis().SetTitleSize(0.05)
  g.GetXaxis().SetTitleOffset(1.06)
  g.GetXaxis().SetTitleFont(42)
  g.GetYaxis().SetTitle("rate (Hz/cm^{2}) ")
  g.GetYaxis().SetLabelFont(42)
  g.GetYaxis().SetLabelOffset(0.008)
  g.GetYaxis().SetLabelSize(0.05)
  g.GetYaxis().SetTitleSize(0.06)
  g.GetYaxis().SetTitleOffset(0.87)
  g.GetYaxis().SetTitleFont(42)

def rollavg( rates_, name, title, ch ):
  rolls = [ "_A", "_B", "_C"]
  rates = []
  h = TH1D(name, title, 36, -0.5, 36.5)
  for i in range(1,37):
    sector = ""
    if i < 10:
      sector = 'CH0'+str(i)
    else:
      sector = 'CH'+str(i)
    rate  = [ float(rates_[ch+sector+r]) for r in rolls]
    #rates.append( float( '%.3f' % np.average(rate) ) )
    h.SetBinContent(i, float( '%.3f' % np.average(rate) ) )
  #return float( '%.3f' % np.average(rate) )
  return h

def main():  
  rpcrateB = RPCRates('316111',"m")
  rpcrateA = RPCRates('323726',"m")
  rpcrateA.rates_ = load_json("ratesAt1p5After.json")
  rpcrateB.rates_ = load_json("ratesAt1p5before.json")

  hREP4A = rollavg( rpcrateA.rates_, "hREP4A", "RE+4/R3", "RE+4_R3_" )
  hREM4A = rollavg( rpcrateA.rates_, "hREM4A", "RE-4/R3", "RE-4_R3_" )

  hREP4B = rollavg( rpcrateB.rates_, "hREP4B", "RE+4/R3", "RE+4_R3_" )
  hREM4B = rollavg( rpcrateB.rates_, "hREM4B", "RE-4/R3", "RE-4_R3_" )

  hsettings(hREP4A); hREP4A.SetLineColor(kBlue)
  hsettings(hREM4A); hREM4A.SetLineColor(kBlue)
  hsettings(hREP4B); hREP4B.SetLineColor(kRed)
  hsettings(hREM4B); hREM4B.SetLineColor(kRed)

  acan = TCanvas("can","",1200,700)

  leg = TLegend(0.645,0.68,0.845,0.88) 
  leg.SetFillStyle( 0 )
  leg.SetBorderSize(0)
  leg.SetMargin( 0.1 )
  
  #leg.AddEntry(hREP4B, "before TS2", "l")
  #leg.AddEntry(hREP4A, "after  TS2", "l")
  #hREP4B.Draw("same hist")
  #hREP4A.Draw("same hist")
  #leg.Draw("same")
  #acan.SaveAs("compREP4.png")
  #acan.Clear()
  #return

  #leg.AddEntry(hREM4B, "before TS2", "l")
  #leg.AddEntry(hREM4A, "after  TS2", "l")
  #hREM4B.Draw("same hist")
  #hREM4A.Draw("same hist")
  #leg.Draw("same")
  #acan.Update()
  #acan.SaveAs("compREM4.png")
  #acan.Clear()
  #return

  hREP4A.Divide(hREP4B)
  hREM4A.Divide(hREM4B)
  hREP4A.SetLineColor(kBlue); hREP4A.SetLineWidth(3)
  hREM4A.SetLineColor(kRed);  hREM4A.SetLineWidth(3)
  hREP4A.GetYaxis().SetTitle("rate ratio")
  hREM4A.GetYaxis().SetTitle("rate ratio")
  hREP4A.SetMaximum(1.5)
  hREM4A.SetMaximum(1.5)
  #leg.AddEntry(hREP4A, "RE+4", "l")
  #leg.AddEntry(hREM4A, "RE-4", "l")
  #hREP4A.Draw("same hist")
  #hREM4A.Draw("same hist")
  #leg.Draw("same")
  #acan.SaveAs("ratiosRE4.png")
  #acan.Clear()
  #return

  mapcreator = RPCMapCreator()  
  histsB = mapcreator.create2Dhistograms( rpcrateB.rates_, 'RPC', "run316111")
  histsA = mapcreator.create2Dhistograms( rpcrateA.rates_, 'RPC', "run323726")
  #prep4_b = histsB["RE+4"].ProjectionX ("rep4b_pfx"); prep4_a = histsA["RE+4"].ProjectionX ("rep4a_pfx")
  #prem4_b = histsB["RE-4"].ProjectionX ("rem4b_pfx"); prem4_a = histsA["RE-4"].ProjectionX ("rem4a_pfx")
  #prep4_b = histsB["RE+4"].ProfileX ("rep4b_pfx"); prep4_a = histsA["RE+4"].ProfileX ("rep4a_pfx")
  #prem4_b = histsB["RE-4"].ProfileX ("rem4b_pfx"); prem4_a = histsA["RE-4"].ProfileX ("rem4a_pfx")
  rep4B = histsB["RE+4"]; rep4A = histsA["RE+4"]
  rem4B = histsB["RE-4"]; rem4A = histsA["RE-4"]

  #prep4_b.SetLineColor(kBlue)
  #prep4_a.SetLineColor(kRed)
  #prem4_b.SetLineColor(kBlue)
  #prem4_a.SetLineColor(kRed)
  #acan.cd()
  rep4A.Divide(rep4B)
  rep4A.SetMaximum(1.1)
  rep4A.SetMinimum(0.9)
  rep4A.Draw("text89 colz")
  acan.SaveAs("ratios2DREP4.png")
  #prep4_b.Draw("same hist")
  #prep4_a.Draw("same hist")

if __name__ == "__main__":
  test = main()
