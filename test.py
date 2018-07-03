from longitude import *

# Needs year, month, day, hour at moment of interest
# Plus the right ascension(RA) of the observer's zenith at the stated time
# Returns estimated longitude

D0 = Julian(2018,7,2)

print("D0 = " + str(D0))

# the time is 3:20
hour = 3.0 + (20.0/60.0)

# GMST - Greenwich Mean Sidereal Time
GMST = GreenwichMST(D0, hour)
print("GMST = " + str(GMST) + " " + str(dd_to_dms(GMST)))
# print("GMST as dms = " + str(dd_to_dms(GMST)))

# GMAT - Greenwich Apparent Sidereal Time
GAST = GreenwichAST(D0, hour, GMST)
print("GAST = " + str(GAST) + " " + str(dd_to_dms(GAST)))
# print("GAST as dms = " + str(dd_to_dms(GAST)))

long = longitude(-33.338504,GAST)

print("long = " + str(long))

dms = dd_to_dms(long)

print("long as dms = " + str(dms))
