#!/usr/bin/env/ python
import sys
import os
import getopt

def main():
  chamberNumbers = ["{0:02d}".format(i+1)  for i in range(12)]
  wheels = ['W+0']
  #wheels = ['W-2', 'W-1', 'W+0', 'W+1', 'W+2']
  RB = ['RB1', 'RB2', 'RB3', 'RB4', 'allRB']
  path = "/afs/cern.ch/work/d/dperezna/public/CMSSW_9_2_15/src/RPC/currentPlots/RSforWheels/"
  os.chdir(path)
  for w in wheels:
    os.chdir(w)
    #os.system('pwd')
    for r in RB:
      os.chdir(r)
      #os.system('pwd')
      queuesDir = 'mkdir queues'
      #print queuesDir
      os.system(queuesDir)
      for c in chamberNumbers:
        if r[-1] == 'B':
          queryBefore = "cbrpc_lumi_feed -d DPID2 -wd '"+w+"' -s '"+c+"' --lhcfill 7080 > queues/beforeTS2AllRB"+c+".csv"
          queryAfter  = "cbrpc_lumi_feed -d DPID2 -wd '"+w+"' -s '"+c+"' --lhcfill 7252 > queues/afterTS2AllRB"+c+".csv"
          #print queryBefore
          #print queryAfter
          os.system(queryBefore)
          os.system(queryAfter)
        else:
          queryBefore = "cbrpc_lumi_feed -d DPID2 -wd '"+w+"' -rs '"+r+"' -s '"+c+"' --lhcfill 7080 > queues/beforeTS2s"+c+".csv"
          queryAfter  = "cbrpc_lumi_feed -d DPID2 -wd '"+w+"' -rs '"+r+"' -s '"+c+"' --lhcfill 7252 > queues/afterTS2s"+c+".csv"
          #print queryBefore
          #print queryAfter
          os.system(queryBefore)
          os.system(queryAfter)
      executeAutomat = "cbrpc_lumi start"
      #print executeAutomat
      os.system(executeAutomat)
      os.chdir('..')
      #os.system('pwd')
    os.chdir(path)
    #os.system('pwd')
  return
if __name__ == "__main__":
  main()
