import copy
from ROOT import TH1F
import math
class RPCRateRun(object):
  """Rate by rolls for a given run""" 
  DISKS  = {-4:"RE-4",-3:"RE-3",-2:"RE-2",-1:"RE-1",1:"RE+1",2:"RE+2",3:"RE+3",4:"RE+4"}
  WHEELS = {-2:"W-2",-1:"W-1",0:"W+0",1:"W+1",2:"W+2"}
  BARREL = {1:"RB1",2:"RB2",3:"RB3",4:"RB4"}
  BARRELs = {1:"RB1in",11:"RB1out",2:"RB2in",21:"RB2out",3:"RB3",4:"RB4"}
  DISKSR = {-4:"RE-4_R2_CH10",-3:"RE-3_R2_CH10",3:"RE+3_R2_CH10",4:"RE+4_R2_CH10"}
  SYSTEM = {"RE-":"RE-","RB":"W","RE+":"RE+"}
  #PATH   = '/Users/dan/detector/RPC/lumiVsRates/TS2_18rates/selRuns18/run' 
  PATH   = '/Users/dan/detector/rates/selRuns18/run'
  ROLLS  = 'output_rolls.json'
  STRIPS = 'output_strips.json'

  def __init__( self, runNumber):
    self.run_    = runNumber
    self.rolls_  = loadJson(self.PATH+str(runNumber)+'/'+self.ROLLS)
    self.strips_ = loadJson(self.PATH+str(runNumber)+'/'+self.STRIPS)
    self.rates_  = copy.deepcopy(self.rolls_['rate'])
    self.errors_ = {}
    self.noisyrolls_ = []
    #self.toexclude_ = []

  def anyToMask(self):
    return bool(self.rolls_['tomask'])

  def correctRates(self,cut):
    for roll in self.rolls_['rate'].keys():
      self.rates_[roll]['ratesquarecm'] = self.removeNoisyStrips(roll,cut)
    return 

  def excludeRolls( self, toexclude):
    for roll in toexclude:
      self.rates_.pop(roll, None)

  def removeNoisyStrips(self,anyroll,cut):
    newrate = 0.0
    h = TH1F(anyroll,anyroll,200,0,1000)
    rollstripinfo = self.strips_['rates'][anyroll]
    activestrips = len(rollstripinfo['rates'])
    noisyroll = False
    for ch2 in rollstripinfo['rates']:
      if float(ch2) > cut: 
        activestrips-=1
        noisyroll = True
        continue
      newrate+=float(ch2)
      h.Fill(float(ch2))
    if noisyroll:
      self.noisyrolls_.append(anyroll)
    if activestrips > 0:
      self.errors_[anyroll] = h.GetStdDev()
      del h
      return str(format(newrate/activestrips,'2f')).decode('unicode-escape')
    else:
      self.errors_[anyroll] = 0.0
      del h
      return str(format(newrate,'2f')).decode('unicode-escape')

  def stripHistograms(self,allrolls):
    hists = {}
    rolls = sorted(self.noisyrolls_)
    if allrolls:
      rolls = self.strips_['rates'].keys()

    for roll in rolls:
      hname = str(self.run_)+"_"+str(roll)
      station = roll.split('_')[0]
      h = TH1F(hname,roll,96,0.5,96.5)
      h.GetXaxis().SetTitle("channels")
      h.GetYaxis().SetTitle("rate [Hz/cm^{2}]")
      for n in range(1,97):
        h.GetXaxis().SetBinLabel(n,str(n))
      h.GetXaxis().SetLabelSize(0.025)
      rollstripinfo = self.strips_['rates'][roll]
      for i,ch in enumerate(rollstripinfo["channels"]):
        h.SetBinContent(int(ch),float(rollstripinfo["rates"][i]))
      try:
        hists[station].append(h)
      except KeyError:
        hists[station] = [h]

    for l in hists.values():
      l.sort()
    return hists

  def averageDisksR(self):
    meanvalues = {}
    for disk in self.DISKSR.keys():
      meanvalues[self.DISKSR[disk]] = self.averagebyDisk(disk)
    return meanvalues
  
  def rateByName(self,name):
      return self.rates_[name]['ratesquarecm']

  def averagebyDisk( self, disk ):
    return self.meanrate( self.DISKS[disk] )

  def averagebyWheel( self, wheel):
    return self.meanrate( self.WHEELS[wheel] )
    
  def averageDisks( self ):
    meanvalues = {}
    for disk in self.DISKS.keys():
      meanvalues[self.DISKS[disk]] = self.averagebyDisk(disk)
    return meanvalues

  def averageWheels( self ):
    meanvalues = {}
    for wheel in self.WHEELS.keys():
      meanvalues[self.WHEELS[wheel]] = self.averagebyWheel(wheel)
    return meanvalues

  def averageBarrel( self ):
    meanvalues = {}
    for station in self.BARREL.keys():
      meanvalues[self.BARREL[station]] = self.meanrate( self.BARREL[station] )
    return meanvalues
  
  def averageBarrels( self ):
    meanvalues = {}
    for station in self.BARRELs.keys():
      meanvalues[self.BARRELs[station]] = self.meanrate( self.BARRELs[station] )
    return meanvalues
  
  def averageSystem( self ):
    meanvalues = {}
    for syst in self.SYSTEM.keys():
      meanvalues[syst] = self.meanrate( self.SYSTEM[syst] )
    return meanvalues

  def averageByS( self, string ):
      return {string:self.meanrate(string)}
  
  def meanFromList( self, mylist ):
    allrates = []
    avgrate = 0.0
    avgerror = 0.0
    for name in mylist:
      allrates.append( [ float(self.rates_[name]["ratesquarecm"]), self.errors_[name] ] )
    for ll in allrates:
      avgrate+=ll[0]
      avgerror+=ll[1]*ll[1]
      avgrate  = avgrate/len(allrates)
      avgerror = math.sqrt(avgerror)/len(allrates)
    return [format(avgrate,'.2f'),format(avgerror,'.2f')]

  def meanrate( self, station ):
    allrates = []
    avgrate = 0.0
    avgerror = 0.0
    for key,value in self.rates_.items():
      if station in key and "inf" not in value["ratesquarecm"]: # and "R1" not in key:
        if float(value["ratesquarecm"]) < 0.0001: continue
        allrates.append( [ float(value["ratesquarecm"]),self.errors_[key] ] )
      #print value
      if len(allrates) > 0:
        for ll in allrates:
          avgrate+=ll[0]
          avgerror+=ll[1]*ll[1]
        avgrate  = avgrate/len(allrates)
        avgerror = math.sqrt(avgerror)/len(allrates)
        #avgrate  = sum(i[0] for i in allrates)/len(allrates)
        #avgerror  = math.sqrt(sum(i[i] for i in allrates))/len(allrates)
      else:
        avgrate  = 0.0
        avgerror = 0.0
    return [format(avgrate,'.2f'),format(avgerror,'.2f')]

def loadJson(ff):
  import json
  with open(ff) as data_file:
    data = json.load(data_file)
  return data
