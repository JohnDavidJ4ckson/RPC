#from os import system, chdir, getcwd
import os
import time
import unittest
import json
import sys

from rhapi import DEFAULT_URL, RhApi

api = RhApi(DEFAULT_URL, debug = False)

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
  try:
    q = "select r.runnumber, r.lhcfill, r.injectionscheme, r.duration, r.initlumi, r.endlumi, r.starttime, r.stoptime"
    q+= " from runreg_global.runs r where r.run_class_name = :class and r.rpc_present = 1 and r.rpc_ready = 1"
    q+= " and r.beam1_present = 1 and r.beam2_present = 1 and r.beam1_stable = 1 and r.beam2_stable = 1 and r.bfield > 3.5"
    q+= " and r.injectionscheme like '25ns%' and r.injectionscheme like '%inj%'" #'%b4e%'" #'%inj%'"
    q+= " and r.duration < 500000 and r.duration > 119" #and r.runnumber > 316057"# and r.runnumber > 306154 "# and r.duration > 1200"
    #q+= " and r.injectionscheme like '25ns' order by r.runnumber desc"
    p = {"class": "Collisions16" }
    qid = api.qid(q)
    #print api.query(qid)
    print api.count(qid, p)
    mydict = api.json(q, p)
    #print mydict
    #quit()
    newdict = {}
    for i,ll in enumerate(mydict[u'data']):
      #if i > 10: break
      #if not os.path.exists(RATEPATH+str(ll[0])):
      #  print "not rate data availabe for run %d " % ll[0]
      #  continue
      if i%10 == 0: print "lumi for ", ll[0]
      lumpltz,lspltz = getLuminosity(ll[0], True, 'pltzero')
      lumhf,lshf = getLuminosity(ll[0], True, 'hfoc')
      #lumd,lsd = getLuminosity(ll[0],False,'')
      dic = {'fill':str(ll[1]),
             'bunches':str(ll[2].split('_')[1].strip('b')),
             'IntsLumiHFOC':str(lumhf),'LSHF':str(lshf),
             #'InstLumiD':str(lumd),'LSD':str(lsd),
             'InstLumiPLTZ':str(lumpltz),'LSPLTZ':str(lspltz),
             'time':str(ll[3]),
             'start':ll[6],
             'stop':ll[7],
             }
      newdict[ll[0]] = dic


    print len(newdict)
    with open('selectedRuns2016.json','w') as ff:
      json.dump(newdict,ff,sort_keys=True,indent=1)
    #print newdict
  except Exception, e:
    print e
    sys.stdout.flush()

if __name__ == '__main__':
  test = main()
