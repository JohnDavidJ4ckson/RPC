#from os import system, chdir, getcwd
import os
import time
import unittest
import json
import sys

from rhapi import DEFAULT_URL, RhApi
RATEPATH = '/afs/cern.ch/work/m/mrodozov/www/Plots/GR2014/run'

def getLuminosity(run, wtype, lumtype):
  instlumi = 0.0
  nls = 0
  if os.path.exists("./lumitemp.csv"): os.system("rm lumitemp.csv")
  if wtype:
    os.system("brilcalc lumi -u 1e30/cm2s -r "+str(run)+" -b 'STABLE BEAMS' --type "+lumtype+" -o lumitemp.csv")
    os.system("brilcalc lumi -u 1e30/cm2s -r "+str(run)+" -b 'STABLE BEAMS' --type "+lumtype+" -o lumitemp.csv")
  else:
    os.system("brilcalc lumi -u 1e30/cm2s -r "+str(run)+" -b 'STABLE BEAMS' -o lumitemp.csv")
  if not os.path.exists("./lumitemp.csv"):
    print "not lumi information for run %d type %s" % (run, lumtype)
    return instlumi,nls
  with open("lumitemp.csv",'rt') as myfile:
    for line in myfile:
      if line.startswith('#'): continue
      else:
        contents =  line.split(',')
        nls = int(contents[2])
        instlumi = float(contents[4])/float(nls)
        break
  return float("{0:.3f}".format(instlumi)),nls

def main():
  import datetime as dt
  try:
    with open("rr3_export_file_2.json") as data_file:
      data = json.load(data_file)
    newdict = {}
    for i,ll in enumerate(data):
      #if i > 10: break
      runnumber  = ll["runNumber"]
      runClass   = ll["runClassName"]
      cmscomment = ll["cms"]["comment"]
      if cmscomment: continue
      bdate = ll["runCreated"].split(" ")[1].split("-")
      btime = ll["runCreated"].split(" ")[2].split(":")
      edate = ll["runModified"].split(" ")[1].split("-")
      etime = ll["runModified"].split(" ")[2].split(":")
      begins = dt.datetime(int("20"+bdate[2]), int(bdate[1]), int(bdate[0]), int(btime[0]), int(btime[1]), int(btime[2]))
      ends = dt.datetime(int("20"+edate[2]), int(edate[1]), int(edate[0]), int(etime[0]), int(etime[1]), int(etime[2]))
      runduration = (ends-begins).seconds
      if runduration < 60 or runduration > 3600: continue
      if not os.path.exists(RATEPATH+str(runnumber)):
        print "not rate data availabe for run %d " % runnumber
        continue
      if i%10 == 0: print "lumi for ", runnumber
      lumpltz,lspltz = getLuminosity(runnumber, True, 'pltzero')
      lumhf,lshf = getLuminosity(runnumber, True, 'hfoc')
      lumd,lsd = getLuminosity(runnumber, False,'')
      dic = {'firunnumber':str(runnumber),
             'IntsLumiHFOC':str(lumhf),'LSHF':str(lshf),
             'InstLumiD':str(lumd),'LSD':str(lsd),
             'InstLumiPLTZ':str(lumpltz),'LSPLTZ':str(lspltz),
             'time':str(runduration)}
      newdict[runnumber] = dic

    print len(newdict)
    with open('selRuns18.json','w') as ff:
      json.dump(newdict,ff,sort_keys=True,indent=1)
    #print newdict'''
  except Exception, e:
    print e
    sys.stdout.flush()

if __name__ == '__main__':
  test = main()
