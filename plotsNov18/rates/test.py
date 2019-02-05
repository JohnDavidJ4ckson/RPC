import os, json
from optparse import OptionParser
from RPCRates import *
from ROOT import * #TFile, TGraph, TMultiGraph, TLegend, TCanvas, TAxis, gStyle, TLatex, TH1D
import math
RATEPATH   = '/afs/cern.ch/work/m/mrodozov/www/Plots/GR2014/run'

def main():
  #run = RPCRates(315489,'m')
  #rw = run.summaryKeys()
  #print run.summaryRates()
  runInfo = {}
  runInfo = load_json('selectedRuns2018.json')

  regr = {}
  rbgr = {}
  wgr  = {}
  rb1ingr = {}
  rb1outgr = {}
  rb2ingr = {}
  rb2outgr = {}
  rb3gr = {}
  rb4gr = {}

  excruns = [ 
              317338,320712,316186,319687,316271,319486,316928,320002,317475,317648,
              317475,317648,317338,319687,320712,316271,317382,316186,319486,316928,
              319678,316993,317434,317212,317475,319950,317648,317319,319941,319459,
              319659
            ]

  j = 0
  for i,run in enumerate(sorted(runInfo.keys())):
    #if j > 15: break
    #if i%10 == 0: 
    #    print i,run
    if int(run) in excruns: continue  
    #if year == 2016 and int(run) > 280385: continue
    if float(runInfo[run]['time']) < 1800: continue 
    if float(runInfo[run]['time']) > 7200: continue
    if int(runInfo[run]['LSPLTZ']) != int(runInfo[run]['LSHF']): continue
    if float(runInfo[run]['bunches']) < 599: continue
    if float(runInfo[run]['InstLumiPLTZ']) < 4000: continue
    if float(runInfo[run]['InstLumiPLTZ']) > 18000: continue
    if not os.path.exists(RATEPATH+str(run)):
      print "not rate lumi for rn %s" %(run)
      continue
    runrate = RPCRates( run, 'm')
    
    fillgraphs( regr, runrate.summaryDisks(),  runInfo[run]['InstLumiPLTZ'], j,run)
    fillgraphs( wgr,  runrate.summaryWheels(), runInfo[run]['InstLumiPLTZ'], j,run)
    fillgraphs( rbgr, runrate.summaryRB(),     runInfo[run]['InstLumiPLTZ'], j,run)
    
    fillgraphs( rb1ingr,  runrate.RBwheel('RB1in'),  runInfo[run]['InstLumiPLTZ'], j,run)
    fillgraphs( rb1outgr, runrate.RBwheel('RB1out'), runInfo[run]['InstLumiPLTZ'], j,run)
    fillgraphs( rb2ingr,  runrate.RBwheel('RB2in'),  runInfo[run]['InstLumiPLTZ'], j,run)
    fillgraphs( rb2outgr, runrate.RBwheel('RB2out'), runInfo[run]['InstLumiPLTZ'], j,run)
    fillgraphs( rb3gr,    runrate.RBwheel('RB3'),    runInfo[run]['InstLumiPLTZ'], j,run)
    fillgraphs( rb4gr,    runrate.RBwheel('RB4'),    runInfo[run]['InstLumiPLTZ'], j,run)
    
    j+=1
    del runrate

  print "+++++++",j
  optsW = {
            'W-2':{'markst':25,'color':634}, 'W+2':{'markst':21,'color':634},
            'W+1':{'markst':22,'color':602}, 'W-1':{'markst':26,'color':602},
            'W+0':{'markst':20,'color':1}
          }             
  optsRB= {
            'RB1in':{'markst':22,'color':602}, 
            'RB1out':{'markst':26,'color':602}, 
            'RB2in':{'markst':21,'color':634},
            'RB2out':{'markst':25,'color':634},
            'RB3':{'markst':22,'color':418},
            'RB4':{'markst':20,'color':1}
           }             
  optsRE = {
            'RE-4':{'markst':24,'color':602}, 'RE-3':{'markst':32,'color':418},
            'RE-2':{'markst':26,'color':634}, 'RE-1':{'markst':25,'color':1},
            'RE+1':{'markst':21,'color':1},   'RE+2':{'markst':22,'color':634},
            'RE+3':{'markst':23,'color':418}, 'RE+4':{'markst':20,'color':602}
           }
  ecsort  = ['RE-4','RE-3','RE-2','RE-1','RE+1','RE+2','RE+3','RE+4']
  whsort  = ['W-2', 'W-1', 'W+0', 'W+1', 'W+2']
  rbsort = ['RB1in', 'RB1out', 'RB2in', 'RB2out','RB3', 'RB4']
  
  rbmax = 20.; remax = 40.
  year = 2018

  printmultigraph(wgr,   whsort,  optsW,  "rvsl_W",   "Barrel wheels",   year, rbmax)
  printmultigraph(rbgr,  rbsort,  optsRB, "rvsl_RB",  "Barrel stations", year, rbmax)
  printmultigraph(regr,   ecsort,  optsRE, "rvsl_RE",  "Endcap stations", year, remax)

  printmultigraph(rb1ingr,   whsort,  optsW,  "rvsl_RB1in",  "RB1in",  year, 40)
  printmultigraph(rb1outgr,  whsort,  optsW,  "rvsl_RB1out", "RB1out", year, 40)
  printmultigraph(rb2ingr,   whsort,  optsW,  "rvsl_RB2in",  "RB2in",  year, 10)
  printmultigraph(rb2outgr,  whsort,  optsW,  "rvsl_RB2out", "RB2out", year, 10)
  printmultigraph(rb3gr,     whsort,  optsW,  "rvsl_RB3",    "RB3",    year, 3)
  printmultigraph(rb4gr,     whsort,  optsW,  "rvsl_RB4",    "RB4",    year, 40)
  
  allgr = wgr.copy()
  allgr.update(rbgr)
  allgr.update(regr)
  allgr.update(rb1ingr)
  allgr.update(rb1outgr)
  allgr.update(rb2ingr)
  allgr.update(rb2outgr)
  allgr.update(rb3gr)
  allgr.update(rb4gr)

  #f=TFile.Open("rvsl_2018.root","RECREATE")
  #f.cd()
  #for k in regr.keys():
  #  regr[k].Write()

def torootFile(grs,name):
  f=TFile.Open(name+".root","RECREATE")
  f.cd()
  for key in grs.keys():
    gr=grs[key]
    gr.SetName(key)
    gr.Write()

def printmultigraph( grs, sortk, plotoptions, outn, title, year, ymax):
  import CMS_lumi, tdrstyle
  import array
  #set the tdr style
  tdrstyle.setTDRStyle()
  
  #change the CMS_lumi variables (see CMS_lumi.py)
  CMS_lumi.writeExtraText = 1 
  CMS_lumi.extraText  = "Preliminary"
  if year == 2018:
    CMS_lumi.extraText2 = "2018 pp data"
  if year == 2017:
    CMS_lumi.extraText2 = "2017 pp data"
  if year == 2016:
    CMS_lumi.extraText2 = "2016 pp data"
  CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
  CMS_lumi.writeTitle = 1 
  CMS_lumi.textTitle = title 

  iPos = 11
  if( iPos==0 ): CMS_lumi.relPosX = 0.12
    
  H_ref = 600; 
  W_ref = 800; 
  W = W_ref
  H = H_ref
  
  iPeriod = 0 
  # references for T, B, L, R
  T = 0.08*H_ref
  B = 0.12*H_ref 
  L = 0.12*W_ref
  R = 0.04*W_ref
  
  c = TCanvas("c", "c", 50, 50, W, H)
  #gStyle.SetOptStat(0)
  c.SetFillColor(0)
  c.SetBorderMode(0)
  c.SetFrameFillStyle(0)
  c.SetFrameBorderMode(0)
  c.SetLeftMargin( L/W )
  c.SetRightMargin( R/W )
  c.SetTopMargin( T/H )
  c.SetBottomMargin( B/H )
  c.SetTickx(0)
  c.SetTicky(0)
  #canvassettings(c)
  
  mg  = TMultiGraph()
  mg.SetTitle(title)
  #gStyle.SetTitleAlign(33)
  leg = TLegend(0.345,0.58,0.645,0.88) 
  leg.SetFillStyle( 0 )
  leg.SetBorderSize(0)
  leg.SetMargin( 0.1 )

  for name in sortk:
    value = plotoptions[name]
    gr = grs[name]
    gr.SetName(name)
    gr.SetMarkerColor(value['color'])
    gr.SetMarkerStyle(value['markst'])
    gr.SetLineColor(value['color'])
    gr.SetMarkerSize(1.15) #1.05
    gr.SetMinimum(0.1)
    mg.Add(gr)
    text = name#+plotoptions[name]['leg']
    leg.AddEntry(gr,text,"p")
  
  mg.SetName(outn)
  mg.SetMinimum(0.1)
  mg.SetMaximum(ymax)#1.6*ymax
  mg.Draw("AP")
  mg.GetXaxis().SetRangeUser(1500,20000)
  mg.Draw("AP")
  c.Update()
  graphAxis(mg)
  
  CMS_lumi.CMS_lumi(c, iPeriod, iPos)
  c.cd()
  c.Update()
  frame = c.GetFrame()
  frame.Draw()
  
  leg.Draw()
  c.SaveAs(outn+".png")
  #c.SaveAs(outn+".C")
  del c

  return

def graphAxis(g):
  g.GetXaxis().SetTitle("Instantaneous Luminosity 10^{30}cm^{-2}#upoints^{-1}")
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

def fillgraphs( graphs, rateinfo, lumi, n, r):
  if not any(graphs):  
    for key in rateinfo.keys():
      gr = TGraph()
      gr.SetName(key)
      graphs[key] = gr
      
  for key in rateinfo.keys():
    graphs[key].Set(n+1)
    graphs[key].SetPoint(n, float(lumi), float(rateinfo[key]))
    latex = TLatex(graphs[key].GetX()[n],graphs[key].GetY()[n],str(r))
    latex.SetTextSize(0.014)
    graphs[key].GetListOfFunctions().Add(latex)
  
  return graphs

def load_json(name):
  with open(name) as data_file:
    data = json.load(data_file)
  return data

if __name__ == "__main__":
    test = main()
