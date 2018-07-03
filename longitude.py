#!/usr/bin/python
# -*- coding: utf-8 -*-
import math as math
import datetime as datetime

# important links
# * http://aa.usno.navy.mil/faq/docs/GAST.php
# * http://aa.usno.navy.mil/siderealtime?year=2018&month=7&day=2&hr=3&min=20&sec=0.0&intv_mag=1.0&intv_unit=1&reps=5&state=AL&place=Auburn

def longitude(RA,GAST):
    long = RA + GAST*15
    return long

# Greenwich Mean Sidereal Time
def GreenwichMST(D0,hour):
    D = float(D0) + float(hour)/24.0

    # T = D/36525 - the number of centuries since the year 2000
    T = float(D)/36525.0

    # GMST = 6.697374558 + 0.06570982441908 D0 + 1.00273790935 H + 0.000026 T2
    GMST = 6.697374558 + (0.06570982441908 * D0) + (1.00273790935 * hour) + (0.000026 * math.pow(T,2))

    # The following alternative formula can be used with a loss of precision of 0.1 second per century:
    # GMST = 18.697374558 + 24.06570982441908*D

    # It will be necessary to reduce GMST to the range 0h to 24h
    GMST = GMST % 24 # maybe this goes to 23?

    return GMST

# Greenwich Apparent Sidereal Time
def GreenwichAST(D0,hour,GMST):
    D     = D0 + float(hour)/24.0

    # ε = 23.4393 - 0.0000004 D
    eps   = 23.4393 - 0.0000004*D

    # L = 280.47 + 0.98565 D.
    L     = 280.47  + 0.98565*D

    # Ω = 125.04 - 0.052954 D
    omega = 125.04 - 0.052954*D

    # Δψ ≈ -0.000319 sin Ω - 0.000024 sin 2L
    delW = -0.000319*math.sin(omega) - 0.000024*math.sin(2.0*L)

    eqeq = delW*math.cos(eps)

    # The correction term is called the nutation in right ascension or the equation of the equinoxes. Thus,
    # GAST = GMST + eqeq.
    GAST = GMST + eqeq
    #GAST = GAST%24
    return GAST

# return number of days passed since noon
# "For both of these Julian dates, compute the number of days and fraction
# (+ or -) from 2000 January 1, 12h UT, Julian date 2451545.0:"
def Julian(year,month,day):
    # julian day value of jan 1 2000 at noon
    # https://astronomy.stackexchange.com/questions/18391/why-is-jd-2451545-0-january-1-2000-noon-instead-of-jd-2451558-0/18394#18394?newreg=3281be391b59402ea2c578ac933f38c1
    jan_1_2000_noon = 2451545.0 # 2451545.0
    # total number of years since Jan 1, 4713 BC
    D0 = ((year+4713.0) * 365.25) + float(days(month)) + float(day) - jan_1_2000_noon
    # print("Julian - year * 365.25 + days(month) + day = " + str(year * 365.25 + days(month) + day))
    return D0

def days(mon):
    dys = [ 0.0, 31.0, 59.0, 90.0, 120.0, 151.0, 181.0, 212.0, 243.0, 273.0, 304.0, 334.0 ]
    return dys[ mon - 1 ]

# https://stackoverflow.com/questions/2579535/how-to-convert-dd-to-dms-in-python
def dd_to_dms(dd):
    min,sec = divmod(dd*3600,60)
    deg,min = divmod(min,60)
    return deg,min,sec
