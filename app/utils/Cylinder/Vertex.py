import math
import Closoid

def ring(r,point_num,center):
    array_v = []
    theata = 0
    fineness = 20
    count = 0
    while True:
        x = r * math.cos(math.pi*fineness*count/360) + center[0]
        y = r * math.sin(math.pi*fineness*count/360) + center[1]
        z = center[2]
        array_v.append([x,y,z])
        if 720 == fineness*count:
            break
        count = count + 1
    return array_v

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
