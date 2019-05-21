# -*- coding: utf-8 -*-
import json
from ROOT import *
from array import array
import CMS_lumi, tdrstyle
import array

def load_json(name):
  with open(name) as data_file:
    data = json.load(data_file)
  return data

def fillgraph( name, points, text):
  n = len(points)
  gr = TGraph(n)
  gr.SetName(name)
  for i,tup in enumerate(points):
    gr.SetPoint(i, tup[1], float(tup[2]))
    if text:
      latex = TLatex(gr.GetX()[i],gr.GetY()[i],str(tup[0]))
      latex.SetTextSize(0.014)
      gr.GetListOfFunctions().Add(latex)
  return gr

def fillgraphs( graphs, rates, lumi, n, r, text):
  if not any(graphs):  
    for key in rates.keys():
      gr = TGraph()
      gr.SetName(key)
      graphs[key] = gr
      
  for key in rates.keys():
    graphs[key].Set(n)
    graphs[key].SetPoint(n, float(lumi), float(rates[key]))
    if text:
      latex = TLatex(graphs[key].GetX()[n],graphs[key].GetY()[n],str(r))
      latex.SetTextSize(0.014)
      graphs[key].GetListOfFunctions().Add(latex)
  
  return graphs

def fitGraph( gr ):
  gr.Fit("pol1","0")
  myfunc = gr.GetFunction("pol1")
  p0=myfunc.GetParameter(0)
  p0err=myfunc.GetParError(0) 
  p1=myfunc.GetParameter(1)
  p1err=myfunc.GetParError(1)

  if p1 < 0.0:
    #return {"slope":0.0,"offset":0.0}
    p1 = 0.0
    p0 = 0.0
  #return {"slope":p1,"offset":p0}
  return p0,p1

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

def printmultigraph( grs, sortk, plotoptions, outn, title, year, ymax):
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
