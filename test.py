from longitude import *

# Needs year, month, day, hour at moment of interest
# Plus the right ascension(RA) of the observer's zenith at the stated time
# Returns estimated longitude

# year, month, day
D0 = Julian(2018,7,2)

print("D0 = " + str(D0))

GMST = GreenwichMST(D0,3.333)

print("GMST = " + str(GMST))

GAST = GreenwichAST(D0,3.3333,GMST)

print("GAST = " + str(GAST))

long = longitude(-33.338504,GAST)

print("long = " + str(long))
