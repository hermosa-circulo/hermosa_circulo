import math
from app.utils import Closoid
def Mapping(c,v):
    for i in range(len(v)):
        for j in range(len(v[0])):
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

def pullV(V,point_num):
    pull_point = [0,50,0]
    stock = []
    num = 0
    for i in range(len(V)):
        flags=1
    if flags==1:
        pull_len= 1*math.pow(0.1,i)
        while len(stock)<point_num:
            min = 100000
            num = 0
            for j in range(len(V[i])):
                distance=50-V[i][j][1]
                if distance < min and not j in stock:
                    min = distance
                    num = j
            stock.append(num)
        s=V[i][stock[0]][1]+pull_len
        elen=1.5
        dd=s-V[i][num][1]
        nn= int(len(stock)/2)
        vs =[]
        ss=99999999
        sum =0
        for j in range(nn):
            vs.append(sum)
            ss = ss*0.9
            sum =sum +ss
        bb = dd/sum
        for j in range(nn):
            vs[j] = vs[j]*bb
        count = len(vs)-1
        for j in range(len(stock)):
            V[i][stock[j]][1]=V[i][stock[j]][1]+vs[count]
            if j%2==1:
                count=count-1
        #   V[0][j][1]=V[0][j][1]+2
    return V
def makeR(x,r,p):
    x = x*p
    if r > x:
        y  = math.sqrt(math.pow(r,2) - math.pow(x,2))
    else:
        y = 0.5
    return y
def makeV(wheel_radius,begining_point,begin,point_num,breast_wide):
    flag = 1
    vertex=[]
    if flag ==1:

        first_point = Closoid.Closoid((math.pi/200)*(0+begining_point))
        #first_point = [0,0]

        first_p2 = Closoid.Closoid((math.pi/200)*(begin+begining_point))
        #first_p2 = [0,0]

        for i in range(150):
            r = makeR(i,wheel_radius,breast_wide)
            point = Closoid.Closoid((math.pi/200)*(i+begining_point))
        center = [0,-(point[0]-first_point[0]-first_p2[0])*100,(point[1]-first_point[1]-first_p2[1])*100]
        #center = [0,0,i*5]
        if begin < i and r > 0.5:
            vertex.append(ring(r,point_num,center))
    #vertex = pullV(vertex,point_num)
    else:
        first_point = [0,0]
        first_p2 = [0,0]
    for i in range(150):
        r = makeR(i,wheel_radius,breast_wide)
        point = [0,0.01*i]
        center = [30,10,i*1]
        if begin < i and r>0.5:
            vertex.append(ring(r,point_num,center))
    vertex = pullV(vertex,point_num)
    return vertex

