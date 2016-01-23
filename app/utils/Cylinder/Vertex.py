import math
import Closoid

def Mapping(c,v):
    for i,row in enumerate(v):
        for j,column in enumerate(row):
            v[i][j] += c[j]
    return v
def ring(r,point_num,center):
    z = 0
    a = 1
    b = 1
    y = -r
    ver = []
    rad = math.tan((math.pi/2))
    x = math.sqrt(r*r/(1/math.pow(a,2)+rad*rad/(b*b)))

    for i in range(point_num*2):
        rad = math.tan((math.pi/point_num)*i)
        x = math.sqrt(math.pow(r,2)/(1/math.pow(a,2)+math.pow(rad,2)/math.pow(b,2)))
        y = math.sqrt((math.pow(r,2)-math.pow(x,2)/math.pow(a,2))/math.pow(b,2))
        if (math.pi/point_num)*i < math.pi/2:
            x = x
            y = y
        elif (math.pi/point_num)*i >= math.pi/2 and (math.pi/point_num)*i < math.pi:
            x = -x
            y = y
        elif (math.pi/point_num)*i >= math.pi and (math.pi/point_num)*i < (math.pi/2)*3:
            x = -x
            y = -y
        else:
            x = x
            y = -y
        ver.append([x,y,z])
    ver = Mapping(center,ver)
    return ver

def makeR(x,r,p):
    x = x*p
    if r > x:
    	y  = math.sqrt(math.pow(r,2) - math.pow(x,2))
    else: 
	    y = 0.5
    return y

def makeV(wheel_radius,begining_point,begin,point_num,breast_wide):
    vertex=[]
    first_point = Closoid.Closoid((math.pi/200)*(0+begining_point))
    first_p2 = Closoid.Closoid((math.pi/200)*(begin+begining_point))

    for i in range(150):
        r = makeR(i,wheel_radius,breast_wide)
        point = Closoid.Closoid((math.pi/200)*(i+begining_point))
        center = [0,-(point[0]-first_point[0]-first_p2[0])*100,(point[1]-first_point[1]-first_p2[1])*100]
        if begin < i and r > 0.5:
            vertex.append(ring(r,point_num,center))

    return vertex
