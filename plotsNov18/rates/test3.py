import os
from optparse import OptionParser
from RPCRates import *
import math
from utils import load_json, fillgraphs, printmultigraph

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
  textRun = False
  for i,run in enumerate(sorted(runInfo.keys())):
    if j >= 15: break
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
    runrate.init()

    fillgraphs( regr, runrate.summaryDisks(),  runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    fillgraphs( wgr,  runrate.summaryWheels(), runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    fillgraphs( rbgr, runrate.summaryRB(),     runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    
    fillgraphs( rb1ingr,  runrate.RBwheel('RB1in'),  runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    fillgraphs( rb1outgr, runrate.RBwheel('RB1out'), runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    fillgraphs( rb2ingr,  runrate.RBwheel('RB2in'),  runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    fillgraphs( rb2outgr, runrate.RBwheel('RB2out'), runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    fillgraphs( rb3gr,    runrate.RBwheel('RB3'),    runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    fillgraphs( rb4gr,    runrate.RBwheel('RB4'),    runInfo[run]['InstLumiPLTZ'], j, run, textRun)
    
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

if __name__ == "__main__":
    test = main()
