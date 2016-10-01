import math
def make_sphere():
    array_v = []
    theata = 0
    radius = 10
    z = 0
    i = 0
    while z <= radius:
        r = math.sqrt(radius*radius - z*z)
        count = 0
        array_v.append([])
        while True:
            x = r * math.cos(math.pi*10*count/360)
            y = r * math.sin(math.pi*10*count/360)
            array_v[i].append([x,y,z])
            if 720 == 10*count:
                break
            count = count + 1
        z = z + 0.2
        i = i + 1
    return array_v

def lattice(array_v):
    point = [[10,10,10],[10,-10,10],[-10,-10,10],[-10,10,10],
             [10,10,0],[10,-10,0],[-10,-10,0],[-10,10,0]]
    point_next = [[10,10,10],[10,-10,10],[-10,-10,10],[-10,10,10],
             [10,10,0],[10,-10,0],[-10,-10,0],[-10,10,0]]
    edge = [[3,1,4],
            [2,0,5],
            [1,3,6],
            [0,2,7],
            [7,5,0],
            [6,4,1],
            [5,7,2],
            [4,6,3]]
    for i in range(len(array_v)):
        for j in range(len(array_v[i])):
            for k in range(len(point)):
                #### x move #####
                x_per = (point_next[k][0]-point[edge[k][0]][0])/(point[k][0]-point[edge[k][0]][0])
                y_per = (array_v[i][j][1]-point[edge[k][1]][1])/(point[k][1]-point[edge[k][1]][1])
                z_per = (array_v[i][j][2]-point[edge[k][2]][2])/(point[k][2]-point[edge[k][2]][2])
                x_next  = point[edge[k][0]][0]+(array_v[i][j][0] - point[edge[k][0]][0])*(1-(1-x_per)*y_per*z_per)
                array_v[i][j][0] = x_next
                #### y move #####
                y_per = (point_next[k][1]-point[edge[k][1]][1])/(point[k][1]-point[edge[k][1]][1])
                x_per = (array_v[i][j][0]-point[edge[k][0]][0])/(point[k][0]-point[edge[k][0]][0])
                z_per = (array_v[i][j][2]-point[edge[k][2]][2])/(point[k][2]-point[edge[k][2]][2])
                y_next  = point[edge[k][1]][1]+(array_v[i][j][1] - point[edge[k][1]][1])*(1-(1-y_per)*x_per*z_per)
                array_v[i][j][1] = y_next
                #### z move #####
                z_per = (point_next[k][2]-point[edge[k][2]][2])/(point[k][2]-point[edge[k][2]][2])
                x_per = (array_v[i][j][0]-point[edge[k][0]][0])/(point[k][0]-point[edge[k][0]][0])
                y_per = (array_v[i][j][1]-point[edge[k][1]][1])/(point[k][1]-point[edge[k][1]][1])
                z_next  = point[edge[k][2]][2]+(array_v[i][j][2] - point[edge[k][2]][2])*(1-(1-z_per)*x_per*y_per)
                array_v[i][j][2] = z_next
    return array_v

def Lattice_obj(): 
    array_v = make_sphere()
    array_v = lattice(array_v)
    str_obj = ""
    ###### Vertices ######
    for i in range(len(array_v)):
        for j in range(len(array_v[i])):
            str_obj += "v "+str(array_v[i][j][0])+" "+str(array_v[i][j][1])+" "+str(array_v[i][j][2])+"\n"
    #### Face #####
    for i in range(len(array_v)-1):
        for j in range(len(array_v[i])-1):
            str_obj += "f "
            str_obj += str(len(array_v[i])*i+j+1)+" "
            str_obj += str(len(array_v[i])*i+j+2)+" "
            str_obj += str(len(array_v[i])*(i+1)+j+2)+"\n"
            str_obj += "f "
            str_obj += str(len(array_v[i])*i+j+1)+" "
            str_obj += str(len(array_v[i])*(i+1)+j+2)+" "
            str_obj += str(len(array_v[i])*(i+1)+j+1)+"\n"
    return str_obj
