from longitude import *
import datetime as datetime

# Needs year, month, day, hour at moment of interest
# Plus the right ascension(RA) of the observer's zenith at the stated time
# Returns estimated longitude

# D0 = Julian(2018,7,2)

now = datetime.datetime.now()
print("now = " + str(now
))
D0 = days_since_julian_epoch(now)
print("D0 = " + str(D0))

# the time is 3:20
hour = now.hour
# hour = 3.0 + (20.0/60.0)

print("hour = " + str(hour))

# GMST - Greenwich Mean Sidereal Time
GMST = GreenwichMST(D0, hour)
print("GMST = " + str(GMST) + " " + str(dd_to_dms(GMST)))
# print("GMST as dms = " + str(dd_to_dms(GMST)))

# GMAT - Greenwich Apparent Sidereal Time
GAST = GreenwichAST(D0, hour, GMST)
print("GAST = " + str(GAST) + " " + str(dd_to_dms(GAST)))
# print("GAST as dms = " + str(dd_to_dms(GAST)))

long = longitude(-33.338504,GAST)

print("long = " + str(long) + " " + str(dd_to_dms(long)))
