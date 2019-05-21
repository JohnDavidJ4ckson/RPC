import os
from optparse import OptionParser
from RPCRates import *
import math
from RPCmapCreator import RPCMapCreator 
from utils import load_json, fillgraphs, printmultigraph, fitGraph
from ROOT import TH1D, TCanvas, kBlue, kRed, TLegend, kBlack, kGreen, kMagenta
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

def diskPhiavg( rates_, disk, ring, name, title ):
  rolls = [ "_A", "_B", "_C"]
  rates = []
  h = TH1D(name, title, 36, -0.5, 36.5)
  for i in range(1,37):
    sector = ""
    if i < 10:
      sector = '_CH0'+str(i)
    else:
      sector = '_CH'+str(i)
    rate  = [ float(rates_[disk+"_"+ring+sector+r]) for r in rolls]
    #rate  = [ float(rates_[disk+"_"+ring+sector+r]) for r in rolls if float(rates_[disk+"_"+ring+sector+r]) > 0.0]
    #rates.append( float( '%.3f' % np.average(rate) ) )
    h.SetBinContent(i, float( '%.3f' % np.average(rate) ) )
  #return float( '%.3f' % np.average(rate) )
  return h

def barrelSectorAvg( rates_, wheel, station, name, title ):
  chamberRB4S04 = [ "++", "+", "-","--"]
  chambersRB3_4 = [ "+", "-"]
  rolls   = [ "_Backward", "_Forward"]
  if station == "RB3":
    rolls   = [ "_Backward", "_Forward", "_Middle"]

  rates = []
  h = TH1D(name, title, 12, 15, 375)
  
  for i in range(1,13):
    lroll = []
    chamber = chambersRB3_4 
    sector = ""
    if i < 10:
      sector = '_S0'+str(i)
    else:
      sector = '_S'+str(i)
    if i == 4: chamber = [ "++", "+", "-","--"]
    elif i == 9: chamber = [ "" ]
    elif i == 11: chamber = [ "" ]
    else: chamber = [ "+", "-"]
    for ch in chamber:
      for r in rolls:
        roll = wheel+"_"+station+ch+sector+r
        lroll.append(roll)
    rate  = [ float(rates_[r]) for r in lroll if float(rates_[r]) > 0.0]
    #rate  = [ float(rates_[r]) for r in lroll]
    print rate
    h.SetBinContent(i, float( '%.3f' % np.average(rate) ) ) if len(rate) > 0 and np.average(rate) < 65.0 else h.SetBinContent(i, 0.0 )
    #h.SetBinContent(i, float( '%.3f' % np.average(rate) ) )
  #return float( '%.3f' % np.average(rate) )
  return h

def phicomparison(rbef,raft,wheel,station,name,title):
  hb = barrelSectorAvg( rbef, wheel, station, name+"_bef", title )
  ha = barrelSectorAvg( raft, wheel, station, name+"_aft", title )
  hsettings(ha); ha.SetLineColor(kBlue); ha.SetLineWidth(3)
  hsettings(hb); hb.SetLineColor(kRed);  hb.SetLineWidth(3)
  
  acan = TCanvas("can","",1200,700)
  leg = TLegend(0.645,0.68,0.845,0.88) 
  leg.SetFillStyle( 0 )
  leg.SetBorderSize(0)
  leg.SetMargin( 0.1 )

  maxx = hb.GetMaximum()
  if maxx < ha.GetMaximum():
    maxx = ha.GetMaximum()

  ha.SetMaximum(1.1*maxx)
  hb.SetMaximum(1.1*maxx)

  leg.AddEntry(ha, "after  TS2", "l")
  leg.AddEntry(hb, "before TS2", "l")
  ha.Draw("same hist")
  hb.Draw("same hist")
  leg.Draw("same")
  acan.SaveAs(name+".png")
  acan.Clear()

  return {"before":hb,"after":ha}

def diskphicomparison(rbef,raft,disk,ring,name,title):
  hb = diskPhiavg( rbef, disk, ring, name+"_bef", title )
  ha = diskPhiavg( raft, disk, ring, name+"_aft", title )
  hsettings(ha); ha.SetLineColor(kBlue); ha.SetLineWidth(2)
  hsettings(hb); hb.SetLineColor(kRed);  hb.SetLineWidth(2)
  
  acan = TCanvas("can","",1200,700)
  leg = TLegend(0.645,0.68,0.845,0.88) 
  leg.SetFillStyle( 0 )
  leg.SetBorderSize(0)
  leg.SetMargin( 0.1 )

  maxx = hb.GetMaximum()
  if maxx < ha.GetMaximum():
    maxx = ha.GetMaximum()

  ha.SetMaximum(1.1*maxx)
  hb.SetMaximum(1.1*maxx)

  leg.AddEntry(ha, "after  TS2", "l")
  leg.AddEntry(hb, "before TS2", "l")
  ha.Draw("same hist")
  hb.Draw("same hist")
  leg.Draw("same")
  acan.SaveAs(name+".png")
  acan.Clear()
  
  return {"before":hb,"after":ha}

def main():
  ratesA_ = load_json("ratesAt1p5after.json")
  ratesB_ = load_json("ratesAt1p5before.json")

  wp2 = phicomparison(ratesB_,ratesA_,"W+2","RB4","compWP2RB4","W+2/RB4")
  wp1 = phicomparison(ratesB_,ratesA_,"W+1","RB4","compWP1RB4","W+1/RB4")
  wp0 = phicomparison(ratesB_,ratesA_,"W+0","RB4","compWP0RB4","W+0/RB4")
  wm1 = phicomparison(ratesB_,ratesA_,"W-1","RB4","compWM1RB4","W-1/RB4")
  wm2 = phicomparison(ratesB_,ratesA_,"W-2","RB4","compWM2RB4","W-2/RB4")
  
  rem4 = diskphicomparison(ratesB_,ratesA_,"RE-4","R3","compREM4R3","RE-4/R3")
  rem3 = diskphicomparison(ratesB_,ratesA_,"RE-3","R3","compREM3R3","RE-3/R3")
  rem2 = diskphicomparison(ratesB_,ratesA_,"RE-2","R3","compREM2R3","RE-2/R3")
  rem1 = diskphicomparison(ratesB_,ratesA_,"RE-1","R3","compREM1R3","RE-1/R3")
  rep1 = diskphicomparison(ratesB_,ratesA_,"RE+1","R3","compREP1R3","RE+1/R3")
  rep2 = diskphicomparison(ratesB_,ratesA_,"RE+2","R3","compREP2R3","RE+2/R3")
  rep3 = diskphicomparison(ratesB_,ratesA_,"RE+3","R3","compREP3R3","RE+3/R3")
  rep4 = diskphicomparison(ratesB_,ratesA_,"RE+4","R3","compREP4R3","RE+4/R3")

  wp2["before"].SetLineColor(kRed+2);  wp2["after"].SetLineColor(kRed+2)
  wp1["before"].SetLineColor(kBlue+2); wp1["after"].SetLineColor(kBlue+2)
  wp0["before"].SetLineColor(kBlack);  wp0["after"].SetLineColor(kBlack)
  wm1["before"].SetLineColor(kGreen+2); wm1["after"].SetLineColor(kGreen+2)
  wm1["before"].SetLineStyle(9);       wm1["after"].SetLineStyle(9)
  wm2["before"].SetLineColor(kMagenta+2);  wm2["after"].SetLineColor(kMagenta+2)
  wm2["before"].SetLineStyle(9);       wm2["after"].SetLineStyle(9)
  
  acan = TCanvas("can","",1200,700)
  acan.Divide(2,1)
  #wp2["after"].Divide(wp2["before"])
  #wp1["after"].Divide(wp1["before"])
  #wp0["after"].Divide(wp0["before"])
  #wm1["after"].Divide(wm1["before"])
  #wm2["after"].Divide(wm2["before"])
  #wp2["after"].SetMaximum(2.5)
  #wp1["after"].SetMaximum(2.5)
  #wp0["after"].SetMaximum(2.5)
  #wm1["after"].SetMaximum(2.5)
  #wm2["after"].SetMaximum(2.5)

  #wp2["after"].SetBarWidth(0.18); wp2["after"].SetBarOffset(0.0); wp2["after"].SetFillColor(kRed+2);
  #h1 = wp2["after"].DrawCopy("bar2");
  #wp1["after"].SetBarWidth(0.18); wp1["after"].SetBarOffset(0.20); wp1["after"].SetFillColor(kBlue+2);
  #h2 = wp1["after"].DrawCopy("bar2 same");
  #wp0["after"].SetBarWidth(0.18); wp0["after"].SetBarOffset(0.40); wp0["after"].SetFillColor(kBlack);
  #h3 = wp0["after"].DrawCopy("bar2 same");
  #wm1["after"].SetBarWidth(0.18); wm1["after"].SetBarOffset(0.60); wm1["after"].SetFillColor(kGreen+2);
  #h4 = wm1["after"].DrawCopy("bar2 same");
  #wp2["after"].SetBarWidth(0.18); wp2["after"].SetBarOffset(0.80); wp2["after"].SetFillColor(kMagenta+2);
  #h5 = wp2["after"].DrawCopy("bar2 same");
  
  acan.cd(1)
  wp2["after"].SetTitle("RB4")
  wp2["after"].Draw("same hist")
  wp1["after"].Draw("same hist")
  wp0["after"].Draw("same hist")
  wm1["after"].Draw("same hist")
  wm2["after"].Draw("same hist")
  
  acan.cd(2)
  wp2["before"].SetTitle("RB4")
  wp2["before"].Draw("same hist")
  wp1["before"].Draw("same hist")
  wp0["before"].Draw("same hist")
  wm1["before"].Draw("same hist")
  wm2["before"].Draw("same hist")

  leg = TLegend(0.345,0.68,0.845,0.88) 
  leg.SetFillStyle( 0 )
  leg.SetBorderSize(0)
  leg.SetMargin( 0.1 )
  leg.AddEntry(wp2["after"], "W+2", "l")
  leg.AddEntry(wp1["after"], "W+1", "l")
  leg.AddEntry(wp0["after"], "W+0", "l")
  leg.AddEntry(wm1["after"], "W-1", "l")
  leg.AddEntry(wm2["after"], "W-2", "l")
  leg.Draw("same")
  
  acan.SaveAs("allwheels.png")
  acan.Clear()

  acan.Divide(2,1)
  acan.cd(1)
  rem4["after"].SetTitle("R3")
  rem4["after"].Draw("same hist")
  rem3["after"].Draw("same hist")
  rem2["after"].Draw("same hist")
  rem1["after"].Draw("same hist")
  
  acan.cd(2)
  rem4["before"].SetTitle("R3")
  rem4["before"].Draw("same hist")
  rem3["before"].Draw("same hist")
  rem2["before"].Draw("same hist")
  rem1["before"].Draw("same hist")

  leg = TLegend(0.345,0.68,0.845,0.88) 
  leg.SetFillStyle( 0 )
  leg.SetBorderSize(0)
  leg.SetMargin( 0.1 )
  leg.AddEntry(rem4["after"], "RE-4", "l")
  leg.AddEntry(rem3["after"], "RE-3", "l")
  leg.AddEntry(rem2["after"], "RE-2", "l")
  leg.AddEntry(rem1["after"], "RE-1", "l")
  leg.Draw("same")
  
  acan.SaveAs("alldisks.png")
  acan.Clear()



  return

if __name__ == "__main__":
  test = main()
