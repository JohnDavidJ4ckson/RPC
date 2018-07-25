import json
import sys
from ROOT import *
from ROOT import gPad


def main():
#  runNumfile = sys.argv[1]
  runNumfile = "output_rolls.json"
  
  with open(runNumfile) as dataf:
    rates1 = json.loads(dataf.read())

  rolls = ["_Backward","_Forward"]
  rates = []
  for roll in rolls:
    rates.append(float(rates1["rate"]["W+0_RB4+_S01"+roll]["ratesquarecm"]))
    print rates
  print sum(rates)/len(rolls)

if __name__ == "__main__":
  test = main() 
