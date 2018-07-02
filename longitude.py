#!/usr/bin/python
# -*- coding: utf-8 -*-
import math as math

# important links
# * http://aa.usno.navy.mil/faq/docs/GAST.php
# * http://aa.usno.navy.mil/siderealtime?year=2018&month=7&day=2&hr=3&min=20&sec=0.0&intv_mag=1.0&intv_unit=1&reps=5&state=AL&place=Auburn

def longitude(RA,GAST):
    long = RA + GAST*15
    return long

# Greenwich Mean Sidereal Time
def GreenwichMST(D0,hour):
    D = D0 + hour/24

    # T = D/36525 - the number of centuries since the year 2000
    T = D/36525

    # GMST = 6.697374558 + 0.06570982441908 D0 + 1.00273790935 H + 0.000026 T2
    GMST = 6.697374558 + (0.06570982441908 * D0) + (1.00273790935 * hour) + 0.000026 * math.pow(T,2)

    # It will be necessary to reduce GMST to the range 0h to 24h
    GMST = GMST % 24

    return GMST

# Greenwich Apparent Sidereal Time
def GreenwichAST(D0,hour,GMST):
    D     = D0 + hour/24

    # ε = 23.4393 - 0.0000004 D
    eps   = 23.4393 - 0.0000004*D

    # L = 280.47 + 0.98565 D.
    L     = 280.47  + 0.98565*D

    # Ω = 125.04 - 0.052954 D
    omega = 125.04 - 0.052954*D

    # Δψ ≈ -0.000319 sin Ω - 0.000024 sin 2L
    delW = -0.000319*math.sin(omega) - 0.000024*math.sin(2*L)

    eqeq = delW*math.cos(eps)

    # The correction term is called the nutation in right ascension or the equation of the equinoxes. Thus,
    # GAST = GMST + eqeq.
    GAST = GMST + eqeq
    #GAST = GAST%24
    return GAST

# return number of days passed since noon
def Julian(year,month,day):
    # julian day value of jan 1 2000 at noon
    jan_1_2000_noon = 2451545.0 # 2451545.0
    D0 = year * 365.25 + days(month) + day - jan_1_2000_noon
    return D0

def days(mon):
    dys = [0,31,59,90.120,151,181,212,243,273,304,334]
    return dys[ mon - 1 ]

# https://stackoverflow.com/questions/2579535/how-to-convert-dd-to-dms-in-python
def dd_to_dms(dd):
    min,sec = divmod(dd*3600,60)
    deg,min = divmod(min,60)
    return deg,min,sec
