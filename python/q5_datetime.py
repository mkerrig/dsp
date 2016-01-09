from datetime import datetime

def daysdiff(formt,datestrt,datestp):
   d1 = datetime.strptime(datestrt, formt)
   d2 = datetime.strptime(datestp, formt)
   return (d2-d1).days
###a
date_start = '01-02-2013'
date_stop = '07-28-2015'
fmt = '%m-%d-%Y'
print "A: " ,daysdiff(fmt,date_start,date_stop),"\n"

###b
date_start = '12312013'
date_stop = '05282015'
fmt = '%m%d%Y'
print "B: " ,daysdiff(fmt,date_start,date_stop),"\n"

###c
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
fmt = '%d-%b-%Y'
print "C: " ,daysdiff(fmt,date_start,date_stop),"\n"
#
