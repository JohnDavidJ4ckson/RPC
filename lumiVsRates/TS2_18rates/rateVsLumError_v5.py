import os, json, math, threading
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import normalize
#from sklearn import metrics
from array import array
from numpy import median
from optparse import OptionParser
from RPCRateRun import *
from ROOT import gPad, TGraph, TGraphErrors,TMultiGraph, TLegend, TCanvas, TAxis, gStyle, TLatex, TFile, TLatex
from ROOT import kGreen, TPaveText, TF1 
RATEPATH   = '/Users/dan/detector/rates/selRuns18/run'

class rate_lumi_fit:
    """
    This class is meant to make the fits automatically
    """

    def __init__(self, previous_info={}):
        wheelKeys_all        = self.keys_wheel_list_all()
        endcapKeys_all       = self.ratesEndcap_list_all()
        wheelKeys_chambers   = self.keys_wheel_list_chambers()
        endcapKeys_chambers  = self.ratesEndcap_list_chambers()
        self.all_subchambers = wheelKeys_all + endcapKeys_all
        self.all_chambers    = wheelKeys_chambers + endcapKeys_chambers
        self.fit_info        = previous_info 
    
                        ###'subchambers': [c for c in all_subchambers if key in c]

    def fit_chamber_and_append_result(self, chamber):
        """
        Perform the MLE of the given chamber
        """
        self.fit_info[chamber] = {}
        subchambers = [c for c in self.all_subchambers if chamber in c]
        lumi, rates = self.create_rate_lumi_list(chamber, subchambers)
        tgr = self.create_tgraph(lumi, rates)
        self.dbscan_for_tgraph(tgr)
        p0, p0_err, p1, p1_err, chi2, ndof, prob = self.fit_tgraph( tgr )
        self.fit_info[chamber]['p0'] = p0
        self.fit_info[chamber]['p0_err'] = p0_err
        self.fit_info[chamber]['p1'] = p1
        self.fit_info[chamber]['p1_err'] = p1_err
        self.fit_info[chamber]['chi2'] = chi2
        self.fit_info[chamber]['ndof'] = ndof
        self.fit_info[chamber]['prob'] = prob

    ### TGraph --> float, float, float, float
    ### This function performs a linear fit and
    ### returns the parameters of interest 
    ### from a given TGraph
    def fit_tgraph( self, gr ):
      
        fun1 = TF1("fun1","pol1",6000,16000)
        fit1 = gr.Fit("fun1","R") # "FQ")
        p0     = fun1.GetParameter(0)
        p0_err = fun1.GetParError(0)
        p1     = fun1.GetParameter(1)
        p1_err = fun1.GetParError(1)
        chi2   = fun1.GetChisquare()
        ndof   = fun1.GetNDF()
        prob   = fun1.GetProb()
        return p0, p0_err, p1, p1_err, chi2, ndof, prob
    
    ### String, list --> list, list
    ### The function receives the name of an RPC chamber and,
    ### a list of the corresponding subchambers. The function
    ### returns two lists. One list with the rates recorded 
    ### and the second list with the corresponding luminosities
    def create_rate_lumi_list(self, chamber, subchambers):
        year = 2018 
        doext = False
        newWp = False
        minrun = 190000
        maxrun = 400000
        maxlum = 20000.0
        maxtime = 7200.0
      
        runInfo = {}
        if year == 2017 and not newWp:
            runInfo = self.load_json('selRuns17.json')
            maxrun = 306155
            maxlum = 14000
        if year == 2018:
            runInfo = self.load_json('selRuns18.json')
            maxlum = 20000
      
        lista_lumi_x = array( 'd' )
        lista_rate_y = array( 'd' )
      
        j = 0
        for i,run in enumerate(sorted(runInfo.keys())):
            try:
                #if i % 50 == 0: print i, run
                #print j
                #if j > 13: break
                #j +=1
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
                #print "PASE LOS CORTES"
                runrate = RPCRateRun( run )
                rate_value = 0
                for c in subchambers:
                    rate_value_temp = float( runrate.rolls_['rate'][c]['ratesquarecm'] )
                    isnan = math.isnan(rate_value_temp)
                    isinf = math.isinf(rate_value_temp)
                    islarge = rate_value_temp > 1000. 
                    #print "checking problem"
                    #print isnan, isinf, islarge
                    if isnan or isinf or islarge: 
                        print "This one is BAD ", run
                        continue
                    rate_value += rate_value_temp
                    continue
                isnan = math.isnan(rate_value)
                isinf = math.isinf(rate_value)
                islarge = rate_value_temp > 10000.
                if isnan or isinf or islarge: continue
                rate_value /= len(subchambers) 
                lumi_value = float( runInfo[run]['InstLumiD'] )
                runrate.correctRates(100.)
                lista_lumi_x.append(lumi_value)
                lista_rate_y.append(rate_value_temp)
            except KeyError:
                continue
            j += 1
            del runrate
        del runInfo
        return lista_lumi_x, lista_rate_y
    
    def create_tgraph(self, listX, listY):
        n = len(listX)
        gr = TGraph(n,listX,listY)
        gr.SetLineColor( 2 )
        gr.SetLineWidth( 4 )
        gr.SetMarkerColor( 6 )
        gr.SetMarkerStyle( 22 )
        gr.SetMarkerSize( 1.5 )
        return gr
    
    def dbscan_for_tgraph(self, v):
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
        self.normalizeToMedian(listaX)
        self.normalizeToMedian(listaY)
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
        #print medianX, medianselfY
        self.reNormalizeToMedian(listaX,medianX)
        self.reNormalizeToMedian(listaY,medianY)
        #print 'Lista Y RE-Normalizada'
        #print len(listaY)
        #for e in listaY: print e
        
        return
    
    def normalizeToMedian(self, array):
        nLenght = len(array)
        arrayMedian = median(array)
        for a in range(nLenght):
            array[a] = array[a] / arrayMedian
        return array
    
    def reNormalizeToMedian(self, array,newMedian):
        #print array
        #print newMedian
        nLenght = len(array)
        #print nLenght
        for a in range(nLenght):
            #print a
            #print array[a] * newMedian
            array[a] = array[a] * newMedian
        #print median(array)
        return array 
    
    ## function to load json data into a dictionary
    def load_json(self, name):
        with open(name) as data_file:
            data = json.load(data_file)
        return data
    
    ### Null -> List
    ### This function creates the keys for every chamber in the Endcap
    ### of the RPC system
    def ratesEndcap_list_all(self):
      rolls = ["_A","_B","_C"] #, "_D"]
      chambers = [
                 "01","02","03","04","05","06","07","08","09",
            "10","11","12","13","14","15","16","17","18","19",
            "20","21","22","23","24","25","26","27","28","29",
            "30","31","32","33","34","35","36"
            ]
      ring = ["_R2", "_R3"]
      disks = ['+4', '+3', '+2', '+1', '-1', '-2', '-3', '-4']
      names = []
      rates = []
      for r in ring:
        for roll in rolls:
          for c in chambers:
            for d in disks:
              try:
                keyValue  = 'RE'+d+r+'_CH'+c+roll
                #print keyValue
                names.append(keyValue)
              except KeyError:
                continue
      #print sorted(names)
      return names
    
    ### Null -> List
    ### This function creates the keys for every chamber in the Endcap
    ### of the RPC system
    def ratesEndcap_list_chambers(self):
      chambers = [
                 "01","02","03","04","05","06","07","08","09",
            "10","11","12","13","14","15","16","17","18","19",
            "20","21","22","23","24","25","26","27","28","29",
            "30","31","32","33","34","35","36"
            ]
      ring = ["_R2", "_R3"]
      disks = ['+4', '+3', '+2', '+1', '-1', '-2', '-3', '-4']
      names = []
      rates = []
      for r in ring:
        for c in chambers:
          for d in disks:
            try:
              keyValue  = 'RE'+d+r+'_CH'+c
              #print keyValue
              names.append(keyValue)
            except KeyError:
              continue
      #print sorted(names)
      return names
    
    
    
    ### Null -> List
    ### This function creates the keys for every chamber in the 
    ### Wheel of the RPC system
    def keys_wheel_list_all(self):
      ## General parameters for geometry
      wheels = ["+2", "+1", "+0", "-1", "-2"]
      stations = [ "01","02","03","04",
                   "05","06","07","08",
                   "09","10","11","12"] 
      ring = ["Forward", "Backward"]
    
      ## Specific names for RB1
      rolls_RB1 = ["RB1in", "RB1out"]
      names_RB1 = ["W"+w+"_"+r+"_S"+st+"_"+ri
                    for w in wheels for r in rolls_RB1
                    for st in stations for ri in ring ]
      ## Specific names for RB2
      ring_RB2_middle   = ["Forward", "Middle", "Backward"]
      wheels_RB2_middle = ["W+1_RB2in", "W-1_RB2in", "W+0_RB2in", "W+2_RB2out", "W-2_RB2out"]
      wheels_RB2        = ["W+2_RB2in", "W-2_RB2in", "W+0_RB2out", "W+1_RB2out", "W-1_RB2out"]
      names_RB2_middle  = [w+"_S"+st+"_"+ri
                            for w in wheels_RB2_middle
                            for st in stations for ri in ring_RB2_middle ]
      names_RB2_nomiddle = [w+"_S"+st+"_"+ri
                             for w in wheels_RB2 
                             for st in stations for ri in ring ]
      names_RB2 = names_RB2_middle + names_RB2_nomiddle 
      ## Specific names for RB3
      rollsRB3 = ["RB3+", "RB3-"]
      names_RB3 = ["W"+w+"_"+r+"_S"+st+"_"+ri 
                    for w in wheels for r in rollsRB3
                    for st in stations for ri in ring ]
      ##Specific names for RB4
      rolls_RB4_double = ["RB4++_S04", "RB4--_S04"]
      names_RB4_double = ["W"+w+"_"+r+"_"+ri
                    for w in wheels for r in rolls_RB4_double
                    for ri in ring ]
      rolls_RB4_null   = ["RB4_S09", "RB4_S11"]
      names_RB4_null = ["W"+w+"_"+r+"_"+ri
                    for w in wheels for r in rolls_RB4_null 
                    for ri in ring ]
      rolls_RB4_normal = ["RB4+", "RB4-"]
      stations_RB4     = [ "01","02","03","04","05",
                           "06","07","08","10","12"]
      names_RB4_normal = ["W"+w+"_"+r+"_S"+s+'_'+ri
                          for w in wheels for r in rolls_RB4_normal 
                          for s in stations_RB4 for ri in ring ]
      names_RB4 = names_RB4_double + names_RB4_null + names_RB4_normal
      
      ## Wrapping up all keys into a single list
      names = names_RB1 + names_RB2 + names_RB3 + names_RB4
      return names 
    
    ### Null -> List
    ### This function creates the keys for every chamber in the 
    ### Wheel of the RPC system
    def keys_wheel_list_chambers(self):
      ## General parameters for geometry
      wheels = ["+2", "+1", "+0", "-1", "-2"]
      stations = [ "01","02","03","04",
                   "05","06","07","08",
                   "09","10","11","12"]
    
      ## Specific names for RB1
      rolls_RB1 = ["RB1in", "RB1out"]
      names_RB1 = ["W"+w+"_"+r+"_S"+st
                    for w in wheels for r in rolls_RB1
                    for st in stations ]
      ## Specific names for RB2
      wheels_RB2_middle = ["W+1_RB2in", "W-1_RB2in", "W+0_RB2in", "W+2_RB2out", "W-2_RB2out"]
      wheels_RB2        = ["W+2_RB2in", "W-2_RB2in", "W+0_RB2out", "W+1_RB2out", "W-1_RB2out"]
      names_RB2_middle  = [w+"_S"+st
                            for w in wheels_RB2_middle
                            for st in stations ]
      names_RB2_nomiddle = [w+"_S"+st
                             for w in wheels_RB2
                             for st in stations ]
      names_RB2 = names_RB2_middle + names_RB2_nomiddle
      ## Specific names for RB3
      rollsRB3 = ["RB3+", "RB3-"]
      names_RB3 = ["W"+w+"_"+r+"_S"+st
                    for w in wheels for r in rollsRB3
                    for st in stations ]
      ##Specific names for RB4
      rolls_RB4_double = ["RB4++_S04", "RB4--_S04"]
      names_RB4_double = ["W"+w+"_"+r
                    for w in wheels for r in rolls_RB4_double ]
      rolls_RB4_null   = ["RB4_S09", "RB4_S11"]
      names_RB4_null = ["W"+w+"_"+r
                    for w in wheels for r in rolls_RB4_null ]
      rolls_RB4_normal = ["RB4+", "RB4-"]
      stations_RB4     = [ "01","02","03","04","05",
                           "06","07","08","10","12"]
      names_RB4_normal = ["W"+w+"_"+r+"_S"+s
                          for w in wheels for r in rolls_RB4_normal
                          for s in stations_RB4 ]
      names_RB4 = names_RB4_double + names_RB4_null + names_RB4_normal
    
      ## Wrapping up all keys into a single list
      names = names_RB1 + names_RB2 + names_RB3 + names_RB4
      return names
    
def main():
  master_info = {}

  ### Now we iterate through the keys and use the
  ### subchambers to fill the rates and lumi lists
  ### That will be used latter for fit
  iii = 0
  for k, v in master_info.items():
      print "This is iii = " + str(iii)
      if iii < 26 or iii > 26:
          iii += 1
          continue
      iii += 1
      print "These are k, v"
      print k, v
      lumi, rates = self.create_rate_lumi_list(k, v['subchambers'])
      tgr = create_tgraph(lumi, rates)
      dbscan_for_tgraph(tgr)
      p0, p0_err, p1, p1_err = fit_tgraph( tgr )
      v['p0'] = p0
      v['p0_err'] = p0_err
      v['p1'] = p1
      v['p1_err'] = p1_err

  with open('lumi_fit_by_chamber.json', 'a') as fp:
    json.dump(master_info, fp, indent=4)
  return


if __name__ == "__main__":
  test = main()

