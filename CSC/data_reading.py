import csv

with open ('CSC_background_at_48_2017_2018.txt', 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter='	', quotechar='|')
  rownum = 0
  colnum = 0
  for row in spamreader:
    #print row #', '.join(row)
    print row
    if rownum == 0:
      header = row
    else:
      colnum = 0

#    for col in row:
      #print type(col)
#      print '%-8s: %s' % (header[colnum], col)

    colnum += 1
    rownum += 1


