#!/usr/bin/env/ python
import sys
import os
import getopt

def main():
  sections = ['030405', '060708', '091011',
              '121314', '151617', '181920',
              '212223', '242526', '272829',
              '303132', '333435', '360102',]
  for s in sections:
    createDirectory = 'mkdir CH'+s
    s1 = 'CH'+s[:2]
    s2 = 'CH'+s[2:4]
    s3 = 'CH'+s[-2:]
    goToDirectory = 'cd CH'+s
    queryBefore = "cbrpc_lumi_feed -d DPID2 -wd 'RE-4' -c '"+s1+"' '"+s2+"' '"+s3+"' --lhcfill 7080 > queues/beforeTS2ch"+s+".csv"
    queryAfter  = "cbrpc_lumi_feed -d DPID2 -wd 'RE-4' -c '"+s1+"' '"+s2+"' '"+s3+"' --lhcfill 7252 > queues/afterTS2ch"+s+".csv"
    executeAutomat = "cbrpc_lumi start"
    restart = "cd /afs/cern.ch/work/d/dperezna/public/CMSSW_9_2_15/src/RPC/currentPlots/RSforRE-4"
    #print createDirectory
    #print goToDirectory
    os.system(queryBefore)
    os.system(queryAfter)
    #print executeAutomat
    #print restart
    #cd directory 
    #cbrpc_lumi_feed -d DPID2 -wd 'RE+4' -c 'CH24' 'CH25' 'CH26' --lhcfill 7080 > queues/beforeTS2Endcap.csv
    #cbrpc_lumi_feed -d DPID2 -wd 'RE+4' -c 'CH24' 'CH25' 'CH26' --lhcfill 7252 > queues/afterTS2Endcap.csv
  os.system('cbrpc_lumi start')

if __name__ == "__main__":
  main()
