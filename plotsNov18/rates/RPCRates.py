# -*- coding: utf-8 -*-
import copy
import numpy as np
import re
from utils import load_json

class RPCRates:
  """RPC Rate for a given run""" 
  RATEPATH   = '/afs/cern.ch/work/m/mrodozov/www/Plots/GR2014/run'
  ROLLS  = 'output_rolls.json'
  STRIPS = 'output_strips.json'
  wheels = ['W-2','W-1','W+0','W+1','W+2']
  disks  = ['RE-4','RE-3','RE-2','RE-1','RE+1','RE+2','RE+3','RE+4']
  barrel = ['RB1in','RB1out','RB2in','RB2out','RB3','RB4']
  rings  = ['R2','R3']
  def __init__( self, runNumber, opt ):
    self.run_      = runNumber
    self.opt_      = opt
    self.sumrolls_ = {}
    self.rates_    = {}
    #@classmethod

  def init( self ):
    if self.opt_ is 'o':
      self.rates_ = load_json(self.RATEPATH+str(runNumber)+'/'+self.ROLLS)['rates']
    elif self.opt_ is 'm':
      self.rates_ = self.initMedian()
    else:
      raise ValueError("measured: o, median m")
    self.sumrolls_ = load_json("RollsForSummary.json")
    print self.run_


  def initMedian( self ):
    outstrips = load_json(self.RATEPATH+str(self.run_)+'/'+self.STRIPS)['rates']
    outrates  = {}
    for roll,d in outstrips.items():
      ratestrip = [ float( format(float(r),'.2f') ) for r in d["rates"]]
      outrates[str(roll)] = float(format(np.median(ratestrip), '.2f'))
    return outrates

  def rateFromList( self, rolls):
    rates = []
    for r in rolls:
      try:
        rates.append(self.rates_[r])
      except KeyError:
        continue
    mm = format(np.median(rates), '.2f') if len(rates)>0 else '0.0'
    return mm

  def summaryDisks( self ):
    rates = {}
    for d in self.disks:
      rates[d] = self.rateFromList( self.sumrolls_[d] )
    return rates
  
  def summaryWheels( self ):
    rates = {}
    for w in self.wheels:
      rates[w] = self.rateFromList( self.sumrolls_[w] )
    return rates
  
  def summaryRB( self ):
    rates = {}
    for r in self.barrel:
      rates[r] = self.rateFromList( self.sumrolls_[r] )
    return rates
  
  def RBwheel( self,  rb ):
    rates = {}
    for w in self.wheels:
      rbw = list(set(self.sumrolls_[rb]).intersection(self.sumrolls_[w]))
      rates[w] = self.rateFromList( rbw )
    return rates

  def summaryKeys( self ):
    wheelsBarrel = []
    for w in self.wheels:
      for b in self.barrel:
        wb = w+'_'+b
        wheelsBarrel.append(wb)

    reg = self.wheels+self.disks+self.barrel+wheelsBarrel
    rollcoll = dict.fromkeys(reg)

    for k in rollcoll.keys():
      rollcoll[k] = []

    for roll in self.rates_.keys():
      for st in reg:
        if st in str(roll):
          rollcoll[st].append(roll)   
    
    with open('RollsForSummary.json', 'w') as outfile:
      json.dump(rollcoll, outfile, sort_keys = True, indent = 4, ensure_ascii = True)
  
  def barrel2Dmap( self ):
    map2D = loadJson("barrelphi.json")
    rates2D = {}
    for k,l in map2D.items():
      rates2D[k] = self.rateFromList( l )
    return rates2D

  def cscformat( self ):
    stationpos = [ "RE+1_R2", "RE+1_R3", "RE+2", "RE+3", "RE+4"]
    stationneg = [ "RE-1_R2", "RE-1_R3", "RE-2", "RE-3", "RE-4"]

    neg = {}
    pos = {}
    for st in stationneg:
      neg[st] = self.inPhi(st)
    for st in stationpos:
      pos[st] = self.inPhi(st)

    return neg,pos

  def inPhi( self, obj ):
    sectors = None
    rates = []
    sectors = [ '0'+str(x) if x<10 else str(x) for x in range(1,37) ]
    if obj.count('_') == 0:
      for s in sectors:
        r2 = obj+"_R2"+"_CH%s" % (s)
        r3 = obj+"_R2"+"_CH%s" % (s)
        rr = np.average( [self.rollavg(r2),self.rollavg(r3)] )
        rates.append(float('%.3f' % rr))
    elif obj.count('_') == 1:
      for s in sectors:
        rr = self.rollavg( obj+"_CH%s" % (s) )
        rates.append(float('%.3f' % rr))
    else:
      rates.append(0.0)
    
    return rates

  def rollavg( self, ch ):
    rolls = [ "_A", "_B", "_C"]
    rate  = [ self.rates_[ch+r] for r in rolls]
    return float( '%.3f' % np.average(rate) )

#def loadJson(ff):
#  with open(ff) as data_file:
#    data = json.load(data_file)
#  return data
