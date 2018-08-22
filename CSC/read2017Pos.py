#!/usr/bin/env python
import re
#from ROOT import *
#from array import array
#from numpy import median
#import numpy as np
#from scipy import stats
import csv

def main():
  with open('cscBackground2017Pos.txt', 'rb') as csvfile:
    keys = ['ME+11', 'ME+12', 'ME+13', 'ME+21', 'ME+22', 'ME+31', 'ME+32', 'ME+41', 'ME+42']
    rates = []
    reader = csv.reader(csvfile, delimiter=',')
    lists = [[] for _ in range(len(keys))]
    for row in reader:
      if row[0] == "Chamber#": continue
      if not row: continue
      for i in range(len(keys)):
        if row[i+1] and float(row[i+1]) != 0: lists[i].append(float(row[i+1]))  
    
    #lengths = [ len(x) for x in lists ]
    #print lengths
  
    rates = [ sum(x)/len(x) for x in lists ]
  #print rates
  #print keys
  
  return rates, keys


if __name__ == "__main__":
  main()


