import os
from optparse import OptionParser
from RPCRates import *
import math
from utils import load_json, fillgraphs, printmultigraph, fillgraph, fitGraph
import json
from ROOT import TFile

RATEPATH   = '/afs/cern.ch/work/m/mrodozov/www/Plots/GR2014/run'

def main():
  #run = RPCRates(315489,'m')
  #rw = run.summaryKeys()
  #print run.summaryRates()
  runInfo = {}
  #runInfo = load_json('selRuns18after.json')
  runInfo = load_json('selRuns18before.json')

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
              319659,323414,323954,323413,323794,324313,323523,323976,323470,324237,
              323978,323775,324237,323693,
              323421,328420,323419,323418,323417,323416,
              322510,322599,322355,322201,322317,
              322605,322602,321906,321815,322599
            ]

  goodruns = [323524,323525,323526,323693,323696,323702,323725,323727,323940,323954,324077,324202,324205,324206,3242,07,324209]

  j = 0
  textRun = False
  textRun = True
  rollgr = {}
  
  for i,run in enumerate(sorted(runInfo.keys())):
    #if j >= 15: break
    #if i%10 == 0: 
    #    print i,run
    if int(run) in excruns: continue  
    #if int(run) not in goodruns: continue  
    #if int(run) < 321500 : continue  
    #if int(run) > 323412 : continue  
    #if int(run) < 321780 : continue  
    #if year == 2016 and int(run) > 280385: continue
    if float(runInfo[run]['time']) < 120: continue 
    #if float(runInfo[run]['time']) > 7200: continue
    #if int(runInfo[run]['LSPLTZ']) != int(runInfo[run]['LSHF']): continue
    if float(runInfo[run]['bunches']) < 599: continue
    #if float(runInfo[run]['InstLumiD']) < 9000: continue
    if float(runInfo[run]['InstLumiD']) > 22500: continue
    if not os.path.exists(RATEPATH+str(run)):
      print "not rate lumi for rn %s" %(run)
      continue
    runrate = RPCRates( run, 'm')
    
    lumival = float(runInfo[run]['InstLumiD'])
    rollrates = runrate.rates_
    for roll in rollrates.keys():
      rate = float(rollrates[roll])
      try:
        rollgr[str(roll)].append([int(run),lumival,rate])
      except KeyError:
        rollgr[str(roll)] = [[int(run),lumival,rate]]
    
    j+=1
    del runrate
    #if j > 10: break

  print "+++++++",j
  
  ff = TFile("rollsgrbefore.root","recreate")
  ff.cd()

  for roll, points in rollgr.items():
    gr = fillgraph(roll,points,textRun)
    gr.Write()
    p0,p1 = fitGraph(gr)
    #rollgr[roll] = format(p0+50000*p1, '.2f')
    rollgr[roll] = format(p0+15000*p1, '.2f')

  with open('ratesAt1p5before.json', 'w') as outfile:
    #json.dump(rollgr, sort_keys = True, indent = 4, ensure_ascii = False)
    json.dump(rollgr, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

def evalRates( d, ev, part):
  print
  print "+++++++++", part
  print
  for k,v in d.items():
    o,s = fitGraph(v)
    print k, o + ev*s

if __name__ == "__main__":
    test = main()
