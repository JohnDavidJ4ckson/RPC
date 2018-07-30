import json
from numpy import median


runNumfile = "output_strips.json"
with open(runNumfile, 'r') as dataf:
  rates1 = json.loads(dataf.read())
print len(rates1)

for k,v in rates1.items():
  print k

new = []
for k,v in rates1["rates"].items():
  list0 = rates1["rates"][k]["rates"]
  newMedianList = []
  #print len(list0)
  for l in range(len(list0)):
    #print len(list0) 
    newMedianList.append(  float( list0[l]) ) 
    #median0 = median( float( list0[l]) )
  #median0 = median( float( list0) )
  median0 = median(newMedianList)
  new.append(median0)
  #print median0
  #print k
  rates1["rates"][k]["ratesquarecm"] = median0

#print len(new)
#print median( new[0])
#print new[2763]

temp = rates1
print "the length of temp is "+str(len(temp))
for k,v in temp.items():
  print k  

with open('data.json', 'w') as outfile:  
    json.dump(temp, outfile)


#  rolls = ["_A","_B","_C"] #, "_D"]
#  chambers = [
#             "01","02","03","04","05","06","07","08","09",
#        "10","11","12","13","14","15","16","17","18","19",
#        "20","21","22","23","24","25","26","27","28","29",
#        "30","31","32","33","34","35","36"
#        ]
#  ring = ["_R2", "_R3"]
#  names = []
#  rates = []
#  for r in ring:
#    for roll in rolls:
#      #rates = []
#      for c in chambers:
#        try:
#          #print r
#          if float(rates1["rate"][endcapSection+r+"_CH"+c+roll]["ratesquarecm"]) == 0: continue
#          rates.append(float(rates1["rate"][endcapSection+r+"_CH"+c+roll]["ratesquarecm"]))
#          names.append(endcapSection+r+"_CH"+c+roll)
#        except KeyError:
#          continue
#  #print sorted(names)
#  return [names, rates]
#
#  wheels = ["0", "1", "2"]
#  rolls = ["1", "2", "3", "4"]
#  subrolls = ["in","out","+","-", "++", "--"]
#  chambers = [
#             "01","02","03","04","05","06",
#             "07","08","09","10","11","12"]
#  ring = ["Forward", "Middle", "Backward"]
#  parameters = ["W+"+w+"_"+wheelSection+s+"_S"+c+"_"+ri for w in wheels
#                for s in subrolls for c in chambers for ri in ring
#                if ( (w == "0") and (ri == "Forward") ) or ( w!="0" )]
#  names = []
#  rates = []
#  for p in parameters:
#    try:
#      if float(rates1["rate"][p]["ratesquarecm"]) == 0: continue
#      rates.append(float(rates1["rate"][p]["ratesquarecm"]))
#      names.append(p)
#    except KeyError:
#      continue
#  return [names, rates]
#
#
