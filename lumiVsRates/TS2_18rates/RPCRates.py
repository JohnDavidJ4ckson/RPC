import copy
from ROOT import TH1F
import math
import numpy as np

class RPCRates(object):
  """RPC Rate for a given run""" 
  RATEPATH   = '/afs/cern.ch/work/m/mrodozov/www/Plots/GR2014/run'
  ROLLS  = 'output_rolls.json'
  STRIPS = 'output_strips.json'

  def __init__( self, runNumber, opt):
    self.run_    = runNumber

    if opt is 'o':
      self.rates_ = loadJson(self.RATEPATH+str(self.run_)+'/'+self.ROLLS)['rates']
    elif opt is 'm':
      self.initMedian()
    else:
      raise ValueError("measured: o, median m")
    print self.run_
    #@classmethod
    #def from_option(cls,opt):

  def initMedian( self ):
    outstrips = loadJson(self.RATEPATH+str(self.run_)+'/'+self.STRIPS)['rates']
    outrates  = {}
    for roll,d in outstrips.items():
      ratestrip = [ float('%.3f' % float(r) ) for r in d["rates"]]
      outrates[str(roll)] = float( '%.3f' % np.median(ratestrip) )
    #return 
    self.rates_ = outrates

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

def loadJson(ff):
  import json
  with open(ff) as data_file:
    data = json.load(data_file)
  return data
