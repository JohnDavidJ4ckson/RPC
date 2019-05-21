import os, json
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import normalize
from sklearn import metrics
from numpy import median
from optparse import OptionParser
from RPCRateRun import *
from ROOT import TGraph, TGraphErrors,TMultiGraph, TLegend, TCanvas, TAxis, gStyle, TLatex, TFile, TLatex
RATEPATH   = '/Users/dan/detector/RPC/lumiVsRates/TS2_18rates/selRuns18/run' 

def main():

  parser = OptionParser()
  parser.add_option("-o", "--outfile", dest="outfile", help="outfile",                       metavar="OUT")
  parser.add_option("-t", "--th",      dest="th",      help="noise threshold",               metavar="TH")
  parser.add_option("-e", "--ext",     dest="doext",   help="extrapolation from linear fit", metavar="EXT")
  parser.add_option("-y", "--year",    dest="year",    help="year",                          metavar="YEAR")
  parser.add_option("-i", "--ifill",   dest="ifill",   help="first fill ",                   metavar="IFILL")
  parser.add_option("-l", "--lfill",   dest="lfill",   help="last fill ",                    metavar="LFILL")
  parser.add_option("-u", "--uncert",  action="store", dest="douncert", help="graphs with uncertainties")
  parser.add_option("-m", "--max",  action="store", dest="yymax", default=True, help="graphs maximum")
  parser.add_option("-w", "--newwp",  action="store", dest="newwp", help="new working pointe")
  
  (options, args) = parser.parse_args()
  year = 2018 #int(options.year)
  doext = False#bool(int(options.doext))
  newWp = False#bool(int(options.newwp))
  minrun = 190000
  maxrun = 400000
  maxlum = 20000.0
  maxtime = 7200.0

  runInfo = {}
  if year == 2017 and newWp:
    runInfo = load_json('selRuns17b4e.json')
    minrun = 306155
    maxtime = 80000
  if year == 2017 and not newWp:
    runInfo = load_json('selRuns17.json')
    maxrun = 306155
    maxlum = 14000
  if year == 2016:
    runInfo = load_json('selRuns16.json')
  if year == 2018:
    runInfo = load_json('selRuns18.json')
    maxlum = 20000
  
  wm2 = ['W-2_RB1in','W-2_RB1out','W-2_RB2in','W-2_RB2out','W-2_RB3','W-2_RB4']
  wm1 = ['W-1_RB1in','W-1_RB1out','W-1_RB2in','W-1_RB2out','W-1_RB3','W-1_RB4']
  wp0 = ['W+0_RB1in','W+0_RB1out','W+0_RB2in','W+0_RB2out','W+0_RB3','W+0_RB4']
  wp1 = ['W+1_RB1in','W+1_RB1out','W+1_RB2in','W+1_RB2out','W+1_RB3','W+1_RB4']
  wp2 = ['W+2_RB1in','W+2_RB1out','W+2_RB2in','W+2_RB2out','W+2_RB3','W+2_RB4']
  re1 = ['RE+1_R1', 'RE+1_R2', 'RE+1_R3']

  wm2gr  = {}
  wm1gr  = {}
  wp0gr  = {}
  wp1gr  = {}
  wp2gr  = {}
  re1gr  = {}

  myrun = [297662,301528,297657,297658,297663,296866,301969,302026,301179,297099,297079,297168,
           297211,297494,300673,301141,301383,300104,299394,297598,300364,297670,296070,296104,
           296114,297664,297659,298997,300812,280241,277126,280383,277093,282708,280023,278289,
           276941,276942,276944,284044,278802,277217,300105,299381,290366,297285,299420,297474,
           300117,300676,299042,302239,300500,296881,297678,300366,297284,300369,300391,300392,
           300394,300396,300397,300369,297169,300365,297715,297009,300365,276836,274970,275289,
           274967,275064,275063,278290,278976,302166,302279,300498,300675,300674,300632,300377,
           300552,300781,300267,300374,300371,300073,300370,300399,300398,300368,300367,300393,
           300395,300390,300234,300106,299327,299326,299324,299318,299317,300107,300283,300373,
           302037,297019,315265,315543,315640,315180,295969,297666,297661,299396,301694,297457,
           299552,300514,300359,300574,300575,300463,300451,300575,300463,300451,300575,299477,
           299450,299316,299178,300375,297281,299552,299000,296702,302159,297180,297179,296782,
           302159,296603,301913,302041,302033,302019,299185,297046,297435,299096,299180,297424,
           297469,297467,300389,299592,300551,300452,300461,300462,300516,302029,300156,299479,
           296663,274282,275656,274382,278873,276092,275757,275886,278273,278285,279681,260327,
           279691,275828,278288,260327,280327,278769,278801,275059,278274,306416,306926,315702,
           315267,315270,315645,315702,315741,315109,315187,315264,315271,316377,315454,315109,
           315187,315150,315454,316109,316277,316186,315151,315154,316271,315179,276456,277180,
           274142,277981,275282,274420,274314,275319,275963,279993,279844,275963,276807,278102,
           276495,276940,278957,279844,278986,278957,279653,278193,280021,274198,278193,280021,
           274198,282917,282031,283305,280239,284025,282033,282712,290239,282842,282730,283933,
           281663,282842,263049,283407,283863,282796,283548,283672,283049,281974,282707,283469,
           301391,301519,297359,297483,299380,299368,296168,296172,300079,301046,301391,297606,
           298996,301519,302228,301281,318828,318810,317479,317080,319077,316715,317319,317479,
           316715,317381,317382,317319,317391,317338,318815,318810,315513,317383,315784,316993,
           317212,317383,317434,317475,317648,318733,318820,318819,316313,318816,318876,318872,
           315557,316926,315555,317068,318876,316926,318816,316613,316928,317088
           ]

  #print "number of runs: ", len(runInfo.keys())
  #print runInfo['323475']
  
  j = 0
  for i,run in enumerate(sorted(runInfo.keys())):
    #print i, run
    #print j
    #if j > 13: break
    if int(run) in myrun: continue  
    if year == 2016 and int(run) > 280385: continue
    if float(runInfo[run]['time']) < 120: continue 
    if float(runInfo[run]['time']) > maxtime: continue
    if float(runInfo[run]['InstLumiD']) < 2000 or float(runInfo[run]['InstLumiD']) > maxlum: continue
    #if float(runInfo[run]['fill']) < firstfill: continue
    #if float(runInfo[run]['fill']) > lastfill: continue
    if int(run) < minrun: continue
    if int(run) > maxrun: continue
    if float(runInfo[run]['bunches']) < 599: continue
    #print RATEPATH+str(run)
    if not os.path.exists(RATEPATH+str(run)):
      continue
    runrate = RPCRateRun( run )
    #print runrate
    #print options.th
    #runrate.correctRates(float(options.th))
    #runrate.excludeRolls(excludedRolls)

    runrate.correctRates(100.)
    means = [{},{},{},{},{},{}]
    for d in range(6):
      #st = d.split('_')[1]
      #print wm2[d]
      #print runrate.averageByS(wm2[d])[wm2[d]]
      #print runrate.averageByS('RE+1_R1')['RE+1_R1']
      means[0][wm2[d].split('_')[1]] = runrate.averageByS(wm2[d])[wm2[d]]
      means[1][wm1[d].split('_')[1]] = runrate.averageByS(wm1[d])[wm1[d]]
      means[2][wp0[d].split('_')[1]] = runrate.averageByS(wp0[d])[wp0[d]]
      means[3][wp1[d].split('_')[1]] = runrate.averageByS(wp1[d])[wp1[d]]
      means[4][wp2[d].split('_')[1]] = runrate.averageByS(wp2[d])[wp2[d]]
      
      continue
    #print re1[0].split('_')[1]
    #print re1[0]
    for d in range(3):
        means[5][re1[d].split('_')[1]] = runrate.averageByS(re1[d])[re1[d]]
        continue
    #print means[4]
    #print means[5]
    #print i,run
    fillgraphs( wm2gr,means[0],runInfo[run]['InstLumiD'],j,run,False )
    fillgraphs( wm1gr,means[1],runInfo[run]['InstLumiD'],j,run,False )
    fillgraphs( wp0gr,means[2],runInfo[run]['InstLumiD'],j,run,False )
    fillgraphs( wp1gr,means[3],runInfo[run]['InstLumiD'],j,run,False )
    fillgraphs( wp2gr,means[4],runInfo[run]['InstLumiD'],j,run,False )
    fillgraphs( re1gr,means[5],runInfo[run]['InstLumiD'],j,run,False ) 

    j+=1
    del runrate
  #ff.Close()
  #rfile.close()
  #quit()
  plotoptionsRB = {
                    'W-2':{'markst':25,'color':634}, 'W+2':{'markst':21,'color':634},
                    'W+1':{'markst':22,'color':602}, 'W-1':{'markst':26,'color':602},
                    'W+0':{'markst':20,'color':1}
                  }             
  plotoptionsRBs= {
                    'RB1in':{'markst':22,'color':602}, 
                    'RB1out':{'markst':26,'color':602}, 
                    'RB2in':{'markst':21,'color':634},
                    'RB2out':{'markst':25,'color':634},
                    'RB3':{'markst':22,'color':418},
                    'RB4':{'markst':20,'color':1}
                  }             
  plotoptionsRE = {'RE-4':{'markst':24,'color':602}, 'RE-3':{'markst':32,'color':418},
                   'RE-2':{'markst':26,'color':634}, 'RE-1':{'markst':25,'color':1},
                   'RE+1':{'markst':21,'color':1},   'RE+2':{'markst':22,'color':634},
                   'RE+3':{'markst':23,'color':418}, 'RE+4':{'markst':20,'color':602}
                  }
  plotoptionsRE1 = {'R1':{'markst':22,'color':602},
                    'R2':{'markst':21,'color':634},
                    'R3':{'markst':20,'color':1},  
                  }

  plotoptionsRPC = {'RE-':{'markst':24,'color':602},'RB':{'markst':23,'color':418}, 'RE+':{'markst':20,'color':602}}

  ecsort   = ['RE-4','RE-3','RE-2','RE-1','RE+1','RE+2','RE+3','RE+4']
  whsort   = ['W-2', 'W-1', 'W+0', 'W+1', 'W+2']
  rbsort   = ['RB1in','RB1out','RB2in','RB2out', 'RB3', 'RB4']
  rpcsort  = ['RE-4','RE-3','RE-2','RE-1','W-2', 'W-1', 'W+0', 'W+1', 'W+2','RE+1','RE+2','RE+3','RE+4']
  syssort  = ['RE-', 'RB', 'RE+']
  ringsort = ['R1', 'R2', 'R3']

  rbmax = 30.; remax = 100.
  if doext:
    rbmax = 45.; remax = 140.
  
  alldics = wm2gr.copy()
  alldics.update(wm1gr)
  alldics.update(wp0gr)
  alldics.update(wp1gr)
  alldics.update(wp2gr)
  alldics.update(re1gr)
  #print alldics
  #print options.outfile
  torootFile(alldics,'name')

  #rateEvalWm2 = printmultigraph(wm2gr, rbsort,  plotoptionsRBs, options.outfile+"_RB_Wm2", "W-2", year, doext, False, rbmax)
  #rateEvalWm1 = printmultigraph(wm1gr, rbsort,  plotoptionsRBs, options.outfile+"_RB_Wm1", "W-1", year, doext, False, 20.0)
  #rateEvalWp0 = printmultigraph(wp0gr, rbsort,  plotoptionsRBs, options.outfile+"_RB_Wp0", "W+0", year, doext, False, 15.0)
  #rateEvalWp1 = printmultigraph(wp1gr, rbsort,  plotoptionsRBs, options.outfile+"_RB_Wp1", "W+1", year, doext, False, 20.0)
  #rateEvalWp2 = printmultigraph(wp2gr, rbsort,  plotoptionsRBs, 'name'+"_RB_Wp2", "W+2", year, doext, False, rbmax)
  
  #print re1gr
  for k, v in re1gr.items():
      #print k
      #print v.GetY()[0]
      listaX  = v.GetX()
      listaY  = v.GetY()
      #print 'Lista Y Sin procesar' 
      #print len(listaY)
      #for e in listaY: print e
      nPoints = v.GetN()
      medianX = median(listaX)
      medianY = median(listaY)
      #print 'Las medians cambian?'
      #print medianX, medianY
      normalizeToMedian(listaX)
      normalizeToMedian(listaY)
      #print 'Lista Y Normalizada'
      #for e in listaY: print e
      zippedXY      = list(map(list,zip(listaX, listaY)))
      clustering    = DBSCAN(eps=0.125, min_samples=15).fit(zippedXY) 
      removedPoints = 0
      for i in range(len(clustering.labels_)):
          cluster = clustering.labels_[i]
          #print cluster
          if cluster == -1:
              v.RemovePoint(i-removedPoints)
              removedPoints += 1
              pass
          continue
      #print 'Las medians cambian?'
      #print medianX, medianY
      reNormalizeToMedian(listaX,medianX)
      reNormalizeToMedian(listaY,medianY)
      #print 'Lista Y RE-Normalizada'
      #print len(listaY)
      #for e in listaY: print e
      del listaX
      del listaY
      del nPoints
      del medianX
      del medianY
      continue

  #mergedXY = zip(listaX, listaY)
  #print mergedXY
  #for e in mergedXY:
  #    print e
  #
  #x2, y2 = zip(*mergedXY)
  #print x2, x2[4]
  #print y2, y2[0]

  rateEvalRe1 = printmultigraph(re1gr, ringsort,  plotoptionsRE1, 'name', 'RE+1', year, doext, False, remax)

  #rateEval = rateEvalRE.copy()
  #rateEval.update(rateEvalRB)
  #rateEval.update(rateEvalRBs)
  #rateEval.update(rateEvalRPC)

def normalizeToMedian(array):
    nLenght = len(array)
    arrayMedian = median(array)
    for a in range(nLenght):
        array[a] = array[a] / arrayMedian
    return array

def reNormalizeToMedian(array,newMedian):
    nLenght = len(array)
    for a in range(nLenght):
        array[a] = array[a] * newMedian
    return 


def createDirs( dirdic,histdic,run,top):
  cdrun  = top.mkdir(run)
  cdstat = []
  #stat = ['RE-4','RE-3','RE-2','RE-1','W-2', 'W-1', 'W+0', 'W+1', 'W+2','RE+1','RE+2','RE+3','RE+4']
  #for s in stat:
  for s in histdic.keys():
    cdstat.append(cdrun.mkdir(s))
  dirdic[run] = {'cdrun':cdrun,'cdstat':cdstat}

def getDir(dirdic,s,h):
  #stat = ['RE-4','RE-3','RE-2','RE-1','W-2', 'W-1', 'W+0', 'W+1', 'W+2','RE+1','RE+2','RE+3','RE+4']
  roll = h.GetTitle()
  idx = 0
  for i,ss in enumerate(dirdic['cdstat']):
    ssname = ss.GetName()
    if ssname in roll:
      idx = i
      break
  return dirdic['cdstat'][idx]

def torootFile(grs,name):
  f=TFile.Open(name+".root","RECREATE")
  f.cd()
  for key in grs.keys():
    gr=grs[key]
    gr.SetName(key)
    gr.Write()
 
def printmultigraph( grs, sortk, plotoptions, outn, title, year, doext, ploterror, ymax):
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
  #gStyle.SetTitleX(0.99)
  leg = TLegend(0.345,0.78,0.645,0.88) #TLegend(1. - c.GetRightMargin() - 0.8, 1. - c.GetTopMargin() - 0.40,1. - c.GetRightMargin()- 0.60, 1. - c.GetTopMargin() -0.02)
  leg.SetFillStyle( 0 )
  leg.SetBorderSize(0)
  leg.SetMargin( 0.1 )
  #ymax = 0;
  ratesFromFit = {}
  evVal = 15000
  if doext:
    evVal = 50000

  #f=TFile.Open(outn+".root","RECREATE")
#  for name,value in plotoptions.iteritems():
  for name in sortk:
    value = plotoptions[name]
    #print grs
    gr = grs[name]
    #print gr
    gr.SetName(name)
    #extrate = fitGraph(gr,evVal)
    #ratesFromFit[name] = extrate
    if doext:
      #print name, extrate[0], extrate[1]
      NN = gr.GetN()
      gr.Set(NN+1)
      gr.SetPoint(NN+1,50000.0,extrate["rate"][0])
      yErr = extrate["rate"][1]
      if not ploterror:
        yErr = 0.0
      gr.SetPointError(NN+1,0.0,yErr)
    gr.SetMarkerColor(value['color'])
    gr.SetMarkerStyle(value['markst'])
    gr.SetLineColor(value['color'])
    gr.SetMarkerSize(1.15) #1.05
    gr.SetMinimum(0.1)
    #gr.Write()
    mg.Add(gr)
    text = name #+plotoptions[name]['leg']
    leg.AddEntry(gr,text,"p")
  
  mg.SetName(outn)
  mg.SetMinimum(0.1)
  mg.SetMaximum(ymax)#1.6*ymax
  mg.Draw("AP")
  mg.GetXaxis().SetRangeUser(2000,20000)
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

  return ratesFromFit

def fitGraph( gr, l):
  
  gr.Fit("pol1","0")
  myfunc = gr.GetFunction("pol1")
  p0=myfunc.GetParameter(0)
  p0err=myfunc.GetParError(0) 
  p1=myfunc.GetParameter(1)
  p1err=myfunc.GetParError(1) 

  #l = 50000.
  rate    = p1*l + p0
  rateErr = math.sqrt(l*l*p1err*p1err + p0err*p0err)
  rate1   = (p1+p1err)*l + (p0+p0err)
  rate2   = (p1-p1err)*l + (p0-p0err)
  diff1   = math.fabs(rate-rate1)
  diff2   = math.fabs(rate-rate2)
  if diff1 <= diff2:
    rateErr = diff2
  else:
    rateErr = diff1

  print "extrapolated rate:", rate, rateErr
  
  return {"rate":[float("{0:.2f}".format(rate)),float("{0:.2f}".format(rateErr))],
          "slope":[float("{0:.8f}".format(p1)),float("{0:.8f}".format(p1err))],
          "offset":[float("{0:.8f}".format(p0)),float("{0:.8f}".format(p0err))]}
  
def printgraph( name, graph ):
  c = TCanvas("Canvas_1", "Canvas_1", 0, 0, 800, 600)
  gStyle.SetOptStat(0)
  canvassettings(c)
  
  graph.SetName(name)
  graph.SetTitle(name)
  graph.SetMarkerColor(4)
  graph.SetMarkerStyle(21)
  graph.SetMarkerSize(1.1)
  graph.SetMinimum(0.1)
  ymax = graph.GetYaxis().GetXmax() 
  graph.SetMaximum(1.3*ymax)
  graphAxis(graph)
  
  graph.Draw("AP")
  sname = str('')
  if "+" in name:
    sname = name.replace("+", "P")
  if "-" in name:
    sname = name.replace("-", "N")
  c.SaveAs(sname+".png")
  c.SaveAs(sname+".C")
  del c

def canvassettings( c ):
  c.SetHighLightColor(2)
  c.SetFillColor(0)
  c.SetBorderMode(0)
  c.SetBorderSize(2)
  c.SetTickx(1)
  c.SetTicky(1)
  c.SetLeftMargin(0.12)
  c.SetRightMargin(0.04)
  c.SetTopMargin(0.08)
  c.SetBottomMargin(0.12)
  c.SetFrameFillStyle(0)
  c.SetFrameBorderMode(0)

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

def fillgraphs( graphs, rateinfo, lumi, n, r, showErr):
  if not any(graphs):
    for key in rateinfo.keys():
      graphs[key] = TGraphErrors()
      
  for key in rateinfo.keys():
    graphs[key].Set(n+1)
    graphs[key].SetPoint(n, float(lumi), float(rateinfo[key][0]))
    xErr = 0.05*float(lumi)
    yErr = float(rateinfo[key][1])
    if not showErr:
      xErr = 0
      yErr = 0
    graphs[key].SetPointError(n, xErr, yErr)
#    latex = TLatex(graphs[key].GetX()[n],graphs[key].GetY()[n],str(r))
#    latex.SetTextSize(0.014)
#    graphs[key].GetListOfFunctions().Add(latex)
  
  return graphs

def load_json(name):
  with open(name) as data_file:
    data = json.load(data_file)
  return data

if __name__ == "__main__":
  test = main()

