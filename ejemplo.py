import json
import sys
from ROOT import *
from ROOT import gPad


def main():
  #runNumfile = sys.argv[1]
  runNumfile = "output_rolls.json" 
  with open(runNumfile) as dataf:
    rates1 = json.loads(dataf.read())

  rolls = ["_A","_B","_C"]
  rates = []
  chamber = [
           "01","02","03","04","05","06","07","08","09",
      "10","11","12","13","14","15","16","17","18","19",
      "20","21","22","23","24","25","26","27","28","29",
      "30","31","32","33","34","35","36"
      ]

  H = 600
  W = 800
  canv = TCanvas("c1", "Canvas", 50, 50, W, H);
  bin = 36
  Hmin = 0
  Hmax = 360
  h1 = TH1F("h4","add bkg sidebans Histograms",bin,Hmin,Hmax);
  
  for c in chamber:
    #print c
    for roll in rolls:
      rates = []
      rates.append(float(rates1["rate"]["RE+1_R2_CH"+c+roll]["ratesquarecm"]))
    x = float(sum(rates)/len(rolls))
    print x
    h1.SetBinContent(int(c),x)
    del x
    print sum(rates)/len(rolls)
   
  h1.Draw()
  h1.SetMarkerColor(2)
  h1.SetMarkerStyle(20)
  h1.SetLineColor(2)
  h1.SetLineWidth(2)
  #h1.GetYaxis().CenterTitle(true)
 #h1->SetYTitle("Pt(J/#psi) [GeV]");
  #h1.SetYTitle(yhname)
 #h1.SetYTitle("Distribution normalized."+yhname);
  #h1.GetXaxis().CenterTitle(true)
  #h1->SetXTitle("|#eta(J/#psi )|"); //#eta(#pi_{Bc}
  #h1.SetXTitle(xhname)#eta(#pi_{Bc}
  #h1.SetTitleSize(35,"XY")
  #h1.SetLabelSize(30,"XY")
  #h1.SetTitleOffset(1.1,"Y")
  #h1.SetTitleOffset(1.0,"X")
  #h1.SetLabelFont(43,"XY")
  #h1.SetTitleFont(43,"XY")
  #h1.SetMinimum(1.0)
  gPad.SetLogy()
  canv.SaveAs("histo.png")


if __name__ == "__main__":
  test = main() 
