import os, json, math
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import normalize
from sklearn import metrics
from array import array
from numpy import median
from optparse import OptionParser
from RPCRateRun import *
from ROOT import gPad, TGraph, TGraphErrors,TMultiGraph, TLegend, TCanvas, TAxis, gStyle, TLatex, TFile, TLatex
from ROOT import kGreen, TPaveText, TF1 
RATEPATH   = '/Users/dan/detector/rates/selRuns18/run'
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


  ## This cases are for an extra test of June 4th
  wheel_helper  = ['_S02', '_S03', '_S04', '_S05', '_S06', '_S07']
  endcap_helper = []
  wp0_test = ['W+0_RB1in','W+0_RB1out','W+0_RB2in','W+0_RB2out','W+0_RB3','W+0_RB4']
  re1_test = ['RE+1_R1', 'RE+1_R2', 'RE+1_R3']
  re2_test = ['RE+1_R1', 'RE+1_R2', 'RE+1_R3']
  re3_test = ['RE+1_R1', 'RE+1_R2', 'RE+1_R3']

  rack76 = ['W+0_RB1in_S02', 'W+0_RB1out_S02',
            'W+0_RB2in_S02', 'W+0_RB2in_S02',
            'W+0_RB3_S02',	
            'W+0_RB4_S02',
            'W+0_RB1in_S03', 'W+0_RB1out_S03',
            'W+0_RB2in_S03', 'W+0_RB2out_S03',
            'W+0_RB3_S03',	
            'W+0_RB4_S03',
            'W+0_RB1in_S04', 'W+0_RB1out_S04',
            'W+0_RB2in_S04', 'W+0_RB2out_S04',
            'W+0_RB3_S04',
            'W+0_RB4_S04',
            'W+0_RB1in_S05', 'W+0_RB1out_S05',
            'W+0_RB2in_S05', 'W+0_RB2out_S05', 
            'W+0_RB3_S05',
            'W+0_RB4_S05',
            'W+0_RB1in_S06', 'W+0_RB1out_S06',
            'W+0_RB2in_S06', 'W+0_RB2out_S06',
            'W+0_RB3_S06',
            'W+0_RB4_S06',
            'W+0_RB1in_S07', 'W+0_RB1out_S07',
            'W+0_RB2in_S07', 'W+0_RB2out_S07',
            'W+0_RB3_S07',
            'W+0_RB4_S07' ]
  
  rack83 = ['RE+1_R2_CH06', 'RE+1_R2_CH11', 
            'RE+1_R2_CH12', 'RE+1_R2_CH17',      
            'RE+1_R2_CH18', 'RE+1_R2_CH23',    
            'RE+1_R2_CH24', 'RE+1_R2_CH29',  
            'RE+1_R2_CH30', 'RE+1_R2_CH35',       
            'RE+1_R2_CH36', 'RE+1_R2_CH05',     
            'RE+1_R3_CH06', 'RE+1_R3_CH11',   
            'RE+1_R3_CH12', 'RE+1_R3_CH17', 
            'RE+1_R3_CH18', 'RE+1_R3_CH23',      
            'RE+1_R3_CH24', 'RE+1_R3_CH29',    
            'RE+1_R3_CH30', 'RE+1_R3_CH35',  
            'RE+1_R3_CH36', 'RE+1_R3_CH05']     

  rack86 = ['RE+4_R2_CH01',  'RE+4_R3_CH01', 'RE+4_R2_CH02', 'RE+4_R3_CH02',   
            'RE+4_R2_CH03',  'RE+4_R3_CH03', 'RE+4_R2_CH04', 'RE+4_R3_CH04',   
            'RE+4_R2_CH05',  'RE+4_R3_CH05', 'RE+4_R2_CH06', 'RE+4_R3_CH06',   
            'RE+4_R2_CH07',  'RE+4_R3_CH07', 'RE+4_R2_CH08', 'RE+4_R3_CH08',   
            'RE+4_R2_CH09',  'RE+4_R3_CH09', 'RE+4_R2_CH10', 'RE+4_R3_CH10',   
            'RE+4_R2_CH11',  'RE+4_R3_CH11', 'RE+4_R2_CH12', 'RE+4_R3_CH12',   
            'RE+4_R2_CH13',  'RE+4_R3_CH13', 'RE+4_R2_CH14', 'RE+4_R3_CH14',   
            'RE+4_R2_CH15',  'RE+4_R3_CH15', 'RE+4_R2_CH16', 'RE+4_R3_CH16',   
            'RE+4_R2_CH17',  'RE+4_R3_CH17', 'RE+4_R2_CH18', 'RE+4_R3_CH18',   
            'RE+4_R2_CH19',  'RE+4_R3_CH19', 'RE+4_R2_CH20', 'RE+4_R3_CH20',   
            'RE+4_R2_CH21',  'RE+4_R3_CH21', 'RE+4_R2_CH22', 'RE+4_R3_CH22',   
            'RE+4_R2_CH35',  'RE+4_R3_CH35', 'RE+4_R2_CH36', 'RE+4_R3_CH36']   
  
  rack68 = ['RE-4_R2_CH01', 'RE-4_R3_CH02',  'RE-4_R2_CH01', 'RE-4_R3_CH02',    
            'RE-4_R2_CH03', 'RE-4_R3_CH04',  'RE-4_R2_CH03', 'RE-4_R3_CH04',    
            'RE-4_R2_CH05', 'RE-4_R3_CH06',  'RE-4_R2_CH05', 'RE-4_R3_CH06',    
            'RE-4_R2_CH07', 'RE-4_R3_CH08',  'RE-4_R2_CH07', 'RE-4_R3_CH08',    
            'RE-4_R2_CH09', 'RE-4_R3_CH10',  'RE-4_R2_CH09', 'RE-4_R3_CH10',    
            'RE-4_R2_CH11', 'RE-4_R3_CH12',  'RE-4_R2_CH11', 'RE-4_R3_CH12',    
            'RE-4_R2_CH13', 'RE-4_R3_CH14',  'RE-4_R2_CH13', 'RE-4_R3_CH14',    
            'RE-4_R2_CH15', 'RE-4_R3_CH16',  'RE-4_R2_CH15', 'RE-4_R3_CH16',    
            'RE-4_R2_CH17', 'RE-4_R3_CH18',  'RE-4_R2_CH17', 'RE-4_R3_CH18',    
            'RE-4_R2_CH19', 'RE-4_R3_CH20',  'RE-4_R2_CH19', 'RE-4_R3_CH20',    
            'RE-4_R2_CH21', 'RE-4_R3_CH22',  'RE-4_R2_CH21', 'RE-4_R3_CH22',    
            'RE-4_R2_CH35', 'RE-4_R3_CH36',  'RE-4_R2_CH35', 'RE-4_R3_CH36']   

  wm2gr  = {}
  wm1gr  = {}
  wp0gr  = {}
  wp1gr  = {}
  wp2gr  = {}
  re1gr  = {}

  rack76gr = {}
  rack83gr = {}
  rack86gr = {}
  rack68gr = {}

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

  listXrack76 = array('d')
  listYrack76 = array('d')
  listXrack83 = array('d')
  listYrack83 = array('d')
  listXrack86 = array('d')
  listYrack86 = array('d')
  listXrack68 = array('d')
  listYrack68 = array('d')

  for i,run in enumerate(sorted(runInfo.keys())):
    #print i, run
    #print j
    #if j > 13: break
    #j +=1
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
    #print runrate.rates_['W+0_RB4+_S01_Forward']['ratesquarecm']
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
      
      #means[0][wm2[d].split('_')[1]] = runrate.averageByS(wm2[d])[wm2[d]]
      #means[1][wm1[d].split('_')[1]] = runrate.averageByS(wm1[d])[wm1[d]]
      means[2][wp0[d].split('_')[1]] = runrate.averageByS(wp0[d])[wp0[d]]
      #means[3][wp1[d].split('_')[1]] = runrate.averageByS(wp1[d])[wp1[d]]
      #means[4][wp2[d].split('_')[1]] = runrate.averageByS(wp2[d])[wp2[d]]
      continue
    #print re1[0].split('_')[1]
    #print re1[0]
    
    rackMeans = [ {}, {}, {}, {} ]
    for d in range(36):
        #print rack76[d].split('_')[1]
        #print rack76[d]
        #print runrate.averageByS(rack76[d])[rack76[d]]
        #print runrate.averageByS(rack76[d])
        #print runrate.averageByS(rack76[d])[rack76[d]]
        #rackMeans[0][rack76[d].split('_')[1]] = runrate.averageByS(rack76[d])[rack76[d]]
        rackMeans[0][rack76[d]] = runrate.averageByS(rack76[d])[rack76[d]]
        #print  rackMeans[0]
        continue
    for d in range(24):
        rackMeans[1][rack83[d]] = runrate.averageByS(rack83[d])[rack83[d]]
        rackMeans[2][rack86[d]] = runrate.averageByS(rack86[d])[rack86[d]]
        continue
    for d in range(48):
        rackMeans[3][rack68[d]] = runrate.averageByS(rack68[d])[rack68[d]]
        continue
    #for d in range(3):
    #    means[5][re1[d].split('_')[1]] = runrate.averageByS(re1[d])[re1[d]]
    #    continue
    
    
    #print means[4]
    #print means[5]
    #print i,run
    #print means[2]
    #print runInfo[run]['InstLumiD']
    
    #fillgraphs( wm2gr,means[0],runInfo[run]['InstLumiD'],j,run,False )
    #fillgraphs( wm1gr,means[1],runInfo[run]['InstLumiD'],j,run,False )
    ###fillgraphs( wp0gr,means[2],runInfo[run]['InstLumiD'],j,run,False )
    #fillgraphs( wp1gr,means[3],runInfo[run]['InstLumiD'],j,run,False )
    #fillgraphs( wp2gr,means[4],runInfo[run]['InstLumiD'],j,run,False )
    ###fillgraphs( re1gr,means[5],runInfo[run]['InstLumiD'],j,run,False ) 



    #rack76gr['main'] = TGraphErrors()
    #rack83gr['main'] = TGraphErrors()
    #rack86gr['main'] = TGraphErrors()
    #rack68gr['main'] = TGraphErrors()


    #print rack76gr
    #print rackMeans[0]
    #print runInfo[run]['InstLumiD']

    lumiValue = float( runInfo[run]['InstLumiD'])
    rateValueList76 = [float(v[0]) for k,v in rackMeans[0].items()]
    rateValue76 = sum(rateValueList76) / len(rateValueList76)
    rateValueList83 = [float(v[0]) for k,v in rackMeans[1].items()]
    rateValue83 = sum(rateValueList83) / len(rateValueList83)
    rateValueList86 = [float(v[0]) for k,v in rackMeans[2].items()]
    rateValue86 = sum(rateValueList86) / len(rateValueList86)
    rateValueList68 = [float(v[0]) for k,v in rackMeans[3].items()]
    rateValue68 = sum(rateValueList68) / len(rateValueList68)

    
    listXrack76.append(lumiValue)
    listYrack76.append(rateValue76)
    listXrack83.append(lumiValue)
    listYrack83.append(rateValue83)
    listXrack86.append(lumiValue)
    listYrack86.append(rateValue86)
    listXrack68.append(lumiValue)
    listYrack68.append(rateValue68)

    
    #print rack76gr['main']
    #print rack83gr['main']
    #print rack86gr['main']
    #print rack68gr['main']
    j += 1
    del runrate
  
  print listXrack76 
  print listYrack83
  print listXrack86
  print listYrack68

  rack76gr = create_tgraph(listXrack76, listYrack76)
  rack83gr = create_tgraph(listXrack83, listYrack83)
  rack86gr = create_tgraph(listXrack86, listYrack86)
  rack68gr = create_tgraph(listXrack68, listYrack68)

  print rack76gr, rack83gr, rack86gr, rack68gr

  dbscan_for_tgraph(rack76gr)
  dbscan_for_tgraph(rack83gr)
  dbscan_for_tgraph(rack86gr)
  dbscan_for_tgraph(rack68gr)


  plot(rack76gr, '76')
  plot(rack83gr, '83')
  plot(rack86gr, '86')
  plot(rack68gr, '68')

  return

## list, string --> Nul
## The function receives a list with TGraphs for each RPC Layer
## and the name of a wheel. These are used to create a plot 
def plot(tgr, n): #(List, layer, tgrDict):
    H = 1600
    W = 800
    #print "----- Creating Third TCanvas -----"
    c = TCanvas("c", "Canvas",W,H)
    ymax = 0.0

    c.SetLeftMargin(0.15);
    c.SetRightMargin(0.06);
    c.SetTopMargin(0.09);
    c.SetBottomMargin(0.14);
    #gPad.SetGrid()
    gPad.SetTicks()
    #gPad.SetLogy()

    mg = TMultiGraph()

    tgr.SetMarkerColor( kGreen+3 )
    tgr.SetMarkerStyle( 21 )
    tgr.SetMarkerSize( 1.5 )
    mg.Add(tgr,'AP')
    mg.Draw("a")

    l = TLegend(0.42,0.15,0.82,0.35)
    l.SetFillColor(0)
    l.SetBorderSize(0)
    l.SetTextSize(0.03)
    l.SetNColumns(1)
    l.AddEntry(tgr, "CMS (13TeV)", "p")

    mg.SetTitle('')
    #mg.SetMaximum(ymax*1.1)
    mg.GetXaxis().SetTitle('Instantaneous Luminosity 10^{34} cm^{-2} s^{-1}')
    mg.GetXaxis().SetLabelFont(42)
    mg.GetXaxis().SetLabelOffset(0.007)
    mg.GetXaxis().SetLabelSize(0.043)
    mg.GetXaxis().SetTitleSize(0.03)
    mg.GetXaxis().SetTitleOffset(1.56)
    mg.GetXaxis().SetTitleFont(42)
    mg.GetYaxis().SetTitle('rate (Hz/cm^{2})')
    mg.GetYaxis().SetLabelFont(42)
    mg.GetYaxis().SetLabelOffset(0.008)
    mg.GetYaxis().SetLabelSize(0.02)
    mg.GetYaxis().SetTitleSize(0.03)
    mg.GetYaxis().SetTitleOffset(1.37)
    mg.GetYaxis().SetTitleFont(42)

    pv = TPaveText(.08,0.94,.45,0.94,"NDC")
    pv.AddText('CMS Preliminary Rack {}'.format(n))
    pv.SetFillStyle(0)
    pv.SetBorderSize(0)
    pv.SetTextSize(0.04)
    pv.Draw()

    fun1 = TF1("fun1","pol1",6000,16000)
    fit1 = tgr.Fit("fun1","R") # "FQ")
    offset1 = fun1.GetParameter(0)
    slope1 = fun1.GetParameter(1)

    l.AddEntry(tgr, 'The p0 value is {0:.6f}'.format(offset1))
    l.AddEntry(tgr, 'The p1 value is {0:.6f}'.format(slope1))

    l.Draw("a")

    c.SaveAs("rack{}.png".format(n))
    c.SaveAs("rack{}.pdf".format(n))
    c.SaveAs("rack{}.C".format(n))
    return 


def create_tgraph(listX, listY):
  n = len(listX)
  gr = TGraph(n,listX,listY)
  gr.SetLineColor( 2 )
  gr.SetLineWidth( 4 )
  gr.SetMarkerColor( 6 )
  gr.SetMarkerStyle( 22 )
  gr.SetMarkerSize( 1.5 )
  return gr


  #ff.Close()
  #rfile.close()
  #quit()
  plotoptionsRB = {
                    'W-2':{'markst':25,'color':634}, 'W+2':{'markst':21,'color':634},
                    'W+1':{'markst':22,'color':602}, 'W-1':{'markst':26,'color':602},
                    'W+0':{'markst':20,'color':1}
                  }             
  plotoptionsRBs= { 'main':{'markst':22,'color':602},
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
  plotoptionsRE1 = {'main':{'markst':22,'color':602},
                    'R1':{'markst':22,'color':602},
                    'R2':{'markst':21,'color':634},
                    'R3':{'markst':20,'color':1},  
                  }

  plotoptionsRPC = {'RE-':{'markst':24,'color':602},'RB':{'markst':23,'color':418}, 'RE+':{'markst':20,'color':602}}

  ecsort   = ['RE-4','RE-3','RE-2','RE-1','RE+1','RE+2','RE+3','RE+4']
  whsort   = ['W-2', 'W-1', 'W+0', 'W+1', 'W+2']
  rbsort   = ['RB1in','RB1out','RB2in','RB2out', 'RB3', 'RB4', 'main']
  rpcsort  = ['RE-4','RE-3','RE-2','RE-1','W-2', 'W-1', 'W+0', 'W+1', 'W+2','RE+1','RE+2','RE+3','RE+4']
  syssort  = ['RE-', 'RB', 'RE+']
  #ringsort = ['R1', 'R2', 'R3']
  ringsort = ['R2', 'R3', 'main']


  rbmax = 30.; remax = 100.
  if doext:
    rbmax = 45.; remax = 140.
  
  alldics = wm2gr.copy()
  alldics.update(wm1gr)
  alldics.update(wp0gr)
  alldics.update(wp1gr)
  alldics.update(wp2gr)
  alldics.update(re1gr)

  alldics.update(rack76gr)
  alldics.update(rack83gr)
  alldics.update(rack86gr)
  alldics.update(rack68gr)

  #print alldics
  #print options.outfile
  torootFile(alldics,'name')

  #rateEvalWm2 = printmultigraph(wm2gr, rbsort,  plotoptionsRBs, options.outfile+"_RB_Wm2", "W-2", year, doext, False, rbmax)
  #rateEvalWm1 = printmultigraph(wm1gr, rbsort,  plotoptionsRBs, options.outfile+"_RB_Wm1", "W-1", year, doext, False, 20.0)
  #rateEvalWp0 = printmultigraph(wp0gr, rbsort,  plotoptionsRBs, "test_RB_Wp0", "W+0", year, doext, False, 15.0)
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

  #dbscan_for_tgraph(rack76gr)
  #dbscan_for_tgraph(rack83gr)
  #dbscan_for_tgraph(rack86gr)
  #dbscan_for_tgraph(rack68gr)

  #print rack76gr['RB1in'].GetN()
  #print rack76gr['RB1out'].GetN()
  #print rack76gr['RB2in'].GetN()
  #print rack76gr['RB2out'].GetN()
  #print rack76gr['RB3'].GetN()
  #print rack76gr['RB4'].GetN()

  ###merge_tgraph_into_one(rack76gr)
  ###merge_tgraph_into_one(rack83gr)
  ###merge_tgraph_into_one(rack86gr)
  ###merge_tgraph_into_one(rack68gr)
  
  #print rack76gr['main'].GetN()
  #print rack83gr['main'].GetN()
  #print rack86gr['main'].GetN()
  #print rack68gr['main'].GetN()
  
 ### dbscan_for_tgraph(rack76gr['main'])
 ### dbscan_for_tgraph(rack83gr['main'])
 ### dbscan_for_tgraph(rack86gr['main'])
 ### dbscan_for_tgraph(rack68gr['main'])

 ## print rack76gr['main'].GetN()
 ## print rack76gr['main'].GetX()
 ## print rack76gr['main'].GetY()
 ## for e in rack76gr['main'].GetX():
 ##     print e
 ## print 'NOW this is Y'
 ## for e in rack76gr['main'].GetY():
 ##     print e
 ## c1 = TCanvas()
 ## rack76gr['main'].Draw()
 ## c1.SaveAs('test_rack76.png')
  
  
  rateEvalRack76 = printmultigraph(rack76gr, rbsort,    plotoptionsRBs, "rack76", "rack76", year, doext, False, 10.0)
  rateEvalRack83 = printmultigraph(rack83gr, ringsort,  plotoptionsRE1, "rack83", "rack83", year, doext, False, 15.0)
  rateEvalRack86 = printmultigraph(rack86gr, ringsort,  plotoptionsRE1, "rack86", "rack86", year, doext, False, 90.0)
  rateEvalRack68 = printmultigraph(rack68gr, ringsort,  plotoptionsRE1, "rack68", "rack68", year, doext, False, 70.0)

  #rateEvalRe1 = printmultigraph(re1gr, ringsort,  plotoptionsRE1, 'name', 'RE+1', year, doext, False, remax)

  #rateEval = rateEvalRE.copy()
  #rateEval.update(rateEvalRB)
  #rateEval.update(rateEvalRBs)
  #rateEval.update(rateEvalRPC)

def merge_tgraph_into_one(rackDict):
    listaX = array( 'd' ) 
    listaY = array( 'd' )
    #print len(listaX)
    #print len(listaY)
    for k,v in rackDict.items():
        #print k
        listaX_temp  = v.GetX()
        listaY_temp  = v.GetY()
        #print listaX
        #print listaY
        for x in listaX_temp:
            listaX.append(x)
            #print x
            continue
        for y in listaY_temp:
            listaY.append(y)
            #print y
            continue
        continue
    #print len(listaX)
    #print len(listaY)
    n = len(listaX)
    
    rackDict['main'] = TGraph(n,listaX,listaY)

    return

def dbscan_for_tgraph(v):
  #print tgraphy
  #for k, v in tgraphy.items():
  
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
  clustering    = DBSCAN(eps=0.100, min_samples=13).fit(zippedXY)
  removedPoints = 0
  for i in range(len(clustering.labels_)):
      #print i
      cluster = clustering.labels_[i]
      #print cluster
      if cluster == -1:
          v.RemovePoint(i-removedPoints)
          removedPoints += 1
          pass
      continue

  listaX  = v.GetX()
  listaY  = v.GetY()
  #print 'Las medians cambian?'
  #print medianX, medianY
  reNormalizeToMedian(listaX,medianX)
  reNormalizeToMedian(listaY,medianY)
  #print 'Lista Y RE-Normalizada'
  #print len(listaY)
  #for e in listaY: print e
  
 # del listaX
 # del listaY
 # del nPoints
 # del medianX
 # del medianY
  
  #continue
  return




def normalizeToMedian(array):
    nLenght = len(array)
    arrayMedian = median(array)
    for a in range(nLenght):
        array[a] = array[a] / arrayMedian
    return array

def reNormalizeToMedian(array,newMedian):
    #print array
    print newMedian
    nLenght = len(array)
    #print nLenght
    for a in range(nLenght):
        #print a
        #print array[a] * newMedian
        array[a] = array[a] * newMedian
    print median(array)
    return array 


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
  #mg  = grs['main']
  mg.SetTitle(title)
  #gStyle.SetTitleAlign(33)
  #gStyle.SetTitleX(0.99)
  leg = TLegend(0.345,0.68,0.645,0.88) #TLegend(1. - c.GetRightMargin() - 0.8, 1. - c.GetTopMargin() - 0.40,1. - c.GetRightMargin()- 0.60, 1. - c.GetTopMargin() -0.02)
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
    if name != 'main': continue
    value = plotoptions[name]
    #print grs
    gr = grs[name]
    #print gr
    gr.SetName(title)
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
    text = title #name #+plotoptions[name]['leg']
    leg.AddEntry(gr,text,"p")
    continue
  
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

  rateValueList    = []
  rateValueListErr = []
  for key, value in rateinfo.items():
      rateNumber = float(value[0])
      rateValueList.append(rateNumber)
      rateNumberErr = float(value[1])
      rateValueListErr.append(rateNumberErr)

      continue
  rateValue    = sum(rateValueList) / len(rateValueList)
  ##errSum = []
  ##for err in rateValueListErr:
  ##    errSum.append(err*err)
  rateValueErr = sum(rateValueListErr) / len(rateValueListErr) 

  #print 'Value an Error are'
  #print rateValue
  #print rateValueErr

  #graphs['main'] = TGraphErrors()
  graphs['main'].Set(n+1)
  graphs['main'].SetPoint(n, float(lumi), float(rateValue))
  xErr = 0.05*float(lumi)
  yErr = float(rateValueErr)
  graphs['main'].SetPointError(n, xErr, yErr)


  ####for key in rateinfo.keys():
  ####  graphs[key].Set(n+1)
  ####  graphs[key].SetPoint(n, float(lumi), float(rateinfo[key][0]))
  ####  xErr = 0.05*float(lumi)
  ####  yErr = float(rateinfo[key][1])
  ####  if not showErr:
  ####    xErr = 0
  ####    yErr = 0
  ####  graphs[key].SetPointError(n, xErr, yErr)
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

