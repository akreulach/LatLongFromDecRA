import math as math

def longitude(RA,GAST):
<<<<<<< HEAD
    biglong = RA - GAST*15
    if biglong > 180:
        long = biglong-360
    elif biglong < -180:
        long = biglong+360
    else:
        long = biglong
=======
    long = RA + GAST*15
>>>>>>> 5b1c90bf1473a8b8be01ff11e8c6f3352f935860
    return long

def GreenwichMST(D0,hour):
    D = D0 + hour/24
    T = D/36525
    GMST = 6.697374558 + 0.06570982441908 * D0 + 1.00273790935*hour + 0.000026 * T * T
    GMST = GMST%24
    return GMST

def GreenwichAST(D0,hour,GMST):
    D   = D0 + hour/24
    eps = 23.4393 - 0.0000004*D
    L   = 280.47  + 0.98565*D
    omg = 125.04  - 0.052954*D
    delW = -0.000319*math.sin(omg) - 0.000024*math.sin(2*L)
    eqeq = delW*math.cos(eps)
    GAST = GMST + eqeq
    return GAST

<<<<<<< HEAD
def Julian(year,month,day): # Adding some provisional 'magic constants'
    D0 = math.floor((year+4712)*365.25) + days(month) + day - 14 - 2451544.5
    return D0

def toDec(hour,minute,second):
    dec = hour + minute/60 + second/3600
    return dec

=======
def Julian(year,month,day): # Adding some provisional 'magic constants 
    D0 = math.floor((year+4712)*365.25) + days(month) + day - 14 - 2451544.5
    return D0

>>>>>>> 5b1c90bf1473a8b8be01ff11e8c6f3352f935860
def days(mon):
    dys = [0,31,59,90,120,151,181,212,243,273,304,334]
    d = dys[mon-1]
    return d
