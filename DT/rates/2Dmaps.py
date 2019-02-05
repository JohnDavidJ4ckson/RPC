import json
import sys
from ROOT import *
from ROOT import gPad

def create2Dhistograms( myMap, datamap, run): 
    with open(myMap) as jsonmap:
        rpcmap = json.loads(jsonmap.read())
    #with open(dataFile) as dataf:
    #    datamap = json.loads(dataf.read())

    hists = {}
    for k,v in rpcmap.iteritems():
        xlabels    = v["Xlabels"]
        ylabels    = v["Ylabels"]
        dimensions = v["BinsAndDimensions"]

        hname  = k+'_'+run#+'_'+HV
        htitle = k+', '+run 
        twoDimensionalHisto = TH2F(hname,htitle,dimensions[0],dimensions[1],dimensions[2],dimensions[3],dimensions[4],dimensions[5])

        for ii in range(len(xlabels)):
            twoDimensionalHisto.GetXaxis().SetBinLabel(ii+1,str(xlabels[ii]))
        for ii in range(len(ylabels)):
            twoDimensionalHisto.GetYaxis().SetBinLabel(ii+1,str(ylabels[ii]))

        coordinates = v["XYcoordinates"]
        for roll,xy in coordinates.iteritems():
            try:
                xx = xy[0]
                yy = xy[1]
                #sRoll = roll.split('_')
                #chname = sRoll[0]+'_'+sRoll[1]+'_'+sRoll[2]
                #dpid = name2dpid[chname]
                #value = float(datamap[dpid][date][HV])
                value = float(datamap[roll])
                twoDimensionalHisto.SetBinContent(xx,yy,value)
            except KeyError:
                continue

        acan = TCanvas(hname+"_can",hname+"_can",1200,700)

        drawopt = "text COLZ"
        #drawopt = "COLZ"
        maxx    = 1.5
        if "RE" in k:
            drawopt = "text89 COLZ"
            #drawopt = "COLZ"
            maxx = 1.5
   
        twoDimensionalHisto.SetStats(False)
        twoDimensionalHisto.SetMinimum(0.5)
        twoDimensionalHisto.SetMaximum(maxx)
        twoDimensionalHisto.Draw(drawopt)
        palette = twoDimensionalHisto.GetListOfFunctions().FindObject("palette")
        twoDimensionalHisto.GetYaxis().SetTitle("Detector Unit")
        twoDimensionalHisto.GetXaxis().SetTitle("Sector")
        twoDimensionalHisto.GetYaxis().SetTitleSize(0.05)
        twoDimensionalHisto.GetYaxis().SetTitleOffset(0.96)
        twoDimensionalHisto.GetYaxis().SetTitleFont(42)
        #twoDimensionalHisto.GetZaxis().SetTitleSize(0.05)
        twoDimensionalHisto.GetZaxis().SetTitleFont(42)
        twoDimensionalHisto.GetZaxis().SetTitleOffset(0.7)
        twoDimensionalHisto.GetZaxis().SetTitle("rate ratio")
      
        tex1 = TLatex(0.11,0.855,"CMS")
        tex1.SetNDC()
        tex1.SetTextFont(61)
        tex1.SetTextSize(0.06)
        tex1.SetLineWidth(2)
        #tex1.Draw("same")
      
        tex2 = TLatex(0.11,0.805,"Preliminary");
        tex2.SetNDC();
        tex2.SetTextAlign(13);
        tex2.SetTextFont(52);
        tex2.SetTextSize(0.0456);
        tex2.SetLineWidth(2);
        #tex2.Draw("same");
        acan.Update()
        nname = ""
        if "+" in k:
            nname = k.replace("+","p")
        if "-" in k:
            nname = k.replace("-","m")
        acan.SaveAs(nname+"_2D"+"_"+run+".png")
        #twoDimensionalHisto.Delete()
        hists[k] = twoDimensionalHisto

    return hists

def getRateRatio( rates1 , rates2 ):
  ratios = {}
  rolls1 = rates1.keys()
  rolls2 = rates2.keys()
  rolls = rolls1

  if (len(rolls2) > len(rolls1)):
    rolls = rolls2

  for roll in rolls1:
    ratio = 0.0 
    num, dem = 0.0, 0.0 
    try: 
      num = float(rates1[roll]["ratesquarecm"])
      den = float(rates2[roll]["ratesquarecm"])
      if den > 0.0:
        ratio = format(num/den,'.2f')
        #ratio = format(num/1.,'.2f')
      else:
        ratio = str(0.0)
      ratios[str(roll)] = ratio
    except KeyError:
      ratios[str(roll)] = ratio

  return ratios

def main():
    myMap  = sys.argv[1]
    mapNum = sys.argv[2]
    mapDen = sys.argv[3]
    
    with open(mapNum) as dataf:
        rates1 = json.loads(dataf.read())
    with open(mapDen) as dataf:
        rates2 = json.loads(dataf.read())

    dataFile = getRateRatio( rates1["rate"] , rates2["rate"] )
    #hrates = create2Dhistograms( myMap, dataFile, str(""))
    hrates = create2Dhistograms( myMap, dataFile, str(""))


if __name__ == "__main__":
    test = main() 
