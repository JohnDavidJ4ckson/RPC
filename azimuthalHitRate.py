import json
import sys
from ROOT import *
from ROOT import gPad


def main():
  #runNumfile = sys.argv[1]
  runNumfile = "output_rolls2018.json" 
  with open(runNumfile) as dataf:
    rates1 = json.loads(dataf.read())

  runNumfile2 = "output_rolls2017.json"
  with open(runNumfile2) as dataf2:
    rates2 = json.loads(dataf2.read())

  H1 = fillHist(rates1)
  H2 = fillHist(rates2)
  
  H1_neg = fillHistNeg(rates1)
  H2_neg = fillHistNeg(rates2)

  createCanvas(H1,H2,H1_neg,H2_neg) 


def createCanvas( h1, h2, h1_neg, h2_neg ):
    H = 1600
    W = 800
    canv = TCanvas("c1", "Canvas", W, H);
    canv.Divide(2)
    #canv = TCanvas()
    ymax = 0.0
    canv.cd(1)

    canv.SetLeftMargin(0.15);
    canv.SetRightMargin(0.06);
    canv.SetTopMargin(0.09);
    canv.SetBottomMargin(0.14);

    gPad.SetGrid()
    gPad.SetLogy()
    for hist in h1:
      if ymax < h1[hist].GetMaximum():
        ymax = h1[hist].GetMaximum()
      h1[hist].SetMarkerColor(2)
      h1[hist].SetMaximum(300)
      h1[hist].Draw("p same hist")
      h1[hist].SetStats(0)
    h1["RE+1_R2"].SetMarkerStyle(26)
    h1["RE+1_R3"].SetMarkerStyle(20)
    h1["RE+2"].SetMarkerStyle(25)
    h1["RE+3"].SetMarkerStyle(23)
    h1["RE+4"].SetMarkerStyle(28) 

    for hist in h2:
      h2[hist].SetMarkerColor(kBlack)
      h2[hist].SetMaximum(300)
      h2[hist].Draw("p same hist")
      h2[hist].SetStats(0)
    h2["RE+1_R2"].SetMarkerStyle(26)
    h2["RE+1_R3"].SetMarkerStyle(20)
    h2["RE+2"].SetMarkerStyle(25)
    h2["RE+3"].SetMarkerStyle(23)
    h2["RE+4"].SetMarkerStyle(28)

    leg0 = TLegend(0.25,0.65,0.4,0.80)
    leg0.SetFillColor(0);
    leg0.SetBorderSize(0);
    leg0.SetTextSize(0.03);
    leg0.AddEntry(h1["RE+1_R2"], "me12", "p")
    leg0.AddEntry(h1["RE+1_R3"], "me13", "p")
    leg0.AddEntry(h1["RE+2"],    "me22",    "p")
    leg0.AddEntry(h1["RE+3"],    "me23",    "p")
    leg0.AddEntry(h1["RE+4"],    "me24",    "p")
    leg0.Draw("same")


    canv.cd(2)
    gPad.SetGrid()
    gPad.SetLogy()

    canv.SetLeftMargin(0.15);
    canv.SetRightMargin(0.06);
    canv.SetTopMargin(0.09);
    canv.SetBottomMargin(0.14);


    for hist in h1_neg:
      if ymax < h1_neg[hist].GetMaximum():
        ymax = h1_neg[hist].GetMaximum()
      h1_neg[hist].SetMarkerColor(2)
      h1_neg[hist].SetMaximum(300)
      h1_neg[hist].Draw("p same hist")
      h1_neg[hist].SetStats(0)
    h1_neg["RE-1_R2"].SetMarkerStyle(26)
    h1_neg["RE-1_R3"].SetMarkerStyle(20)
    h1_neg["RE-2"].SetMarkerStyle(25)
    h1_neg["RE-3"].SetMarkerStyle(23)
    h1_neg["RE-4"].SetMarkerStyle(28)

    for hist in h2_neg:
      h2_neg[hist].SetMarkerColor(kBlack)
      h2_neg[hist].SetMaximum(300)
      h2_neg[hist].Draw("p same hist")
      h2_neg[hist].SetStats(0)
    h2_neg["RE-1_R2"].SetMarkerStyle(26)
    h2_neg["RE-1_R3"].SetMarkerStyle(20)
    h2_neg["RE-2"].SetMarkerStyle(25)
    h2_neg["RE-3"].SetMarkerStyle(23)
    h2_neg["RE-4"].SetMarkerStyle(28)


    leg = TLegend(0.25,0.65,0.4,0.80)
    leg.SetFillColor(0);
    leg.SetBorderSize(0);
    leg.SetTextSize(0.03);
    leg.AddEntry(h1["RE+1_R2"], "me12", "p")
    leg.AddEntry(h1["RE+1_R3"], "me13", "p")
    leg.AddEntry(h1["RE+2"],    "me22",    "p")
    leg.AddEntry(h1["RE+3"],    "me23",    "p")
    leg.AddEntry(h1["RE+4"],    "me24",    "p")

    leg.Draw("same")

    canv.SaveAs("histo.pdf")
    canv.SaveAs("histo.png")
    canv.SaveAs("histo.gif")
    return 0

def fillHist( rates2 ):
    bin = 36
    Hmin = 0
    Hmax = 360
    h1_2 = TH1F("h12","+z Endcap",bin,Hmin,Hmax)
    h1_3 = TH1F("h13","+z Endcap",bin,Hmin,Hmax)
    h2 = TH1F("h2",   "+z Endcap",bin,Hmin,Hmax)
    h3 = TH1F("h3",   "+z Endcap",bin,Hmin,Hmax)
    h4 = TH1F("h4",   "+z Endcap",bin,Hmin,Hmax)
    #print "in the function "
    rolls = ["_A","_B","_C"]
    chamber = [
             "01","02","03","04","05","06","07","08","09",
        "10","11","12","13","14","15","16","17","18","19",
        "20","21","22","23","24","25","26","27","28","29",
        "30","31","32","33","34","35","36"
        ]
    ring = ["_R2", "_R3"]
    ll = [ "RE+1", "RE+2", "RE+3", "RE+4"]
# Histrograms dictionary
    dictio = {}
    for l in ll:
      #if l != "RE+1":
      print l
      print dictio
  # Loop to fill all the sub-Rings R1, R2 DOES NOT APPLY FOR Section1
      for r in ring:
        if l != "RE+1":
          h = TH1F("h{}".format(l),"+z Endcap",bin,Hmin,Hmax)
          dictio[l] = h
        else:
          h = TH1F("h{}{}".format(l,r),"+z Endcap",bin,Hmin,Hmax)
          dictio[l+r] = h
        print r
    # Loop to fill the Histogram Bins (36 chambers)
        for c in chamber:
          print c
    # Loop to take the average over sub-chambers ABC
          rates = []
          for roll in rolls:
            #rates = []
            rates.append(float(rates2["rate"][l+r+"_CH"+c+roll]["ratesquarecm"]))
            print rates
          x = float(sum(rates)/len(rates))
          print x
          if l != "RE+1":
            dictio[l].SetBinContent(int(c),x)
            print len(rates)
          else:
            print len(rates)
            dictio[l+r].SetBinContent(int(c),x) 
          del x
          #print sum(rates)/len(rates)
    print dictio
    return dictio     

def fillHistNeg( rates2 ):
    bin = 36
    Hmin = 0
    Hmax = 360
    h1_2 = TH1F("h12","-z Endcap",bin,Hmin,Hmax)
    h1_3 = TH1F("h13","-z Endcap",bin,Hmin,Hmax)
    h2 = TH1F("h2",   "-z Endcap",bin,Hmin,Hmax)
    h3 = TH1F("h3",   "-z Endcap",bin,Hmin,Hmax)
    h4 = TH1F("h4",   "-z Endcap",bin,Hmin,Hmax)
    #print "in the function "
    rolls = ["_A","_B","_C"]
    chamber = [
             "01","02","03","04","05","06","07","08","09",
        "10","11","12","13","14","15","16","17","18","19",
        "20","21","22","23","24","25","26","27","28","29",
        "30","31","32","33","34","35","36"
        ]
    ring = ["_R2", "_R3"]
    ll = [ "RE-1", "RE-2", "RE-3", "RE-4"]
# Histrograms dictionary
    dictio = {}
    for l in ll:
      #if l != "RE+1":
      print l
      print dictio
  # Loop to fill all the sub-Rings R1, R2 DOES NOT APPLY FOR Section1
      for r in ring:
        if l != "RE-1":
          h = TH1F("h{}".format(l),"-z Endcap",bin,Hmin,Hmax)
          dictio[l] = h
        else:
          h = TH1F("h{}{}".format(l,r),"-z Endcap",bin,Hmin,Hmax)
          dictio[l+r] = h
        print r
    # Loop to fill the Histogram Bins (36 chambers)
        for c in chamber:
          print c
    # Loop to take the average over sub-chambers ABC
          rates = []
          for roll in rolls:
            #rates = []
            rates.append(float(rates2["rate"][l+r+"_CH"+c+roll]["ratesquarecm"]))
            print rates
          x = float(sum(rates)/len(rates))
          print x
          if l != "RE-1":
            dictio[l].SetBinContent(int(c),x)
            print len(rates)
          else:
            print len(rates)
            dictio[l+r].SetBinContent(int(c),x)
          del x
          #print sum(rates)/len(rates)
    print dictio
    return dictio


if __name__ == "__main__":
  test = main() 
