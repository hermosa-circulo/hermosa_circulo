import math
from app.utils.Cylinder import Vertex
def VectorSubstruction(v1,v2):
    ans = [0 for i in range(len(v1))]
    for i in range(len(v1)):
        ans[i] = v1[i]-v2[i]
    return ans
def CrossProduct(a,b):
    ans = [0 for i in range(len(a))]
    ans[0] = (a[1]*b[2]-a[2]*b[1])
    ans[1] = (a[2]*b[0]-a[0]*b[2])
    ans[2] = (a[0]*b[1]-a[1]*b[0])
    return ans

def returnV(wheel_radius,begining_point,closoid_number,point_num,breast_wide):
    v1 = [[[0,0,0],[10,0,0],[10,10,0],[0,10,0]],
        [[0,0,10], [10,0,10],[10,10,10],[0,10,10]]]
    v = Vertex.makeV(wheel_radius,begining_point,closoid_number,point_num,breast_wide)
    center = [0,0,0]
    return v

def returnVN(v):
    vn =[[[0 for i in range(3)]for j in range(len(v[0]))]for k in range(len(v)-1)]
    for i in range(len(v)-1):
        for j in range(len(v[0])):
            if j == len(v[0])-1:
                a = VectorSubstruction(v[i][j],v[i+1][j])
                b = VectorSubstruction(v[i][j],v[i][0])
                vn[i][j] = CrossProduct(a,b)
            else:
                a = VectorSubstruction(v[i][j],v[i+1][j])
                b = VectorSubstruction(v[i][j],v[i][j+1])
                vn[i][j] = CrossProduct(a,b)
    return vn

def returnF(v,vn):
    f = [["" for i in range(len(vn[0]))]for i in range(len(vn))]
    for i in range(len(v)-1):
        vnum0 = i*len(v[0])+1
        vnum1 = (i+1)*len(v[0])+1
        for j in range(len(v[0])):
            if j == len(v[0])-1:
                f[i][j] = "f "+str(vnum0)+"//"+str(vnum0+j)+" "+str(vnum1)+"//"+str(vnum0+j)+" "+str(vnum1+j)+"//"+str(vnum0+j)+" "+str(vnum0+j)+"//"+str(vnum0+j)+"\n"
            else:
                f[i][j] = "f "+str(vnum0+j+1)+"//"+str(vnum0+j)+" "+str(vnum1+j+1)+"//"+str(vnum0+j)+" "+str(vnum1+j)+"//"+str(vnum0+j)+" "+str(vnum0+j)+"//"+str(vnum0+j)+"\n"
    return f

def CapV(v,jud):
    if jud == 0:
        point = 0
    else:
        point = len(v)-1

    a = VectorSubstruction(v[point][0],v[point][1])
    b = VectorSubstruction(v[point][0],v[point][2])
    vncap= CrossProduct(a,b)
    if jud ==0:
        for i in range(len(vncap)):
            vncap[i]=-vncap[i]
    return vncap

def CapF(v,vn,jud):
    if jud == 0:
        point = 1
        vnpoint = (len(vn))*len(vn[0])+1
    else:
        point = (len(v)-1)*len(v[0])+1
        vnpoint = (len(vn))*len(vn[0])+2
    fcap = ""
    for i in range(len(v[0])-2):
        fcap += "f "+str(point)+"//"+str(vnpoint)+" "+str(point+i+1)+"//"+str(vnpoint)+" "+str(point+i+2)+"//"+str(vnpoint)+("\n")
    return fcap

def make(wheel_radius,begining_point,closoid_number,point_num,breast_wide):
    #parameter.closoid_number = 30
    ring=2
    v = returnV(wheel_radius,begining_point,closoid_number,point_num,breast_wide)
    vn = returnVN(v)
    f = returnF(v,vn)
    vncap = CapV(v,1)
    fcap = CapF(v,vn,1)
    vncap_first = CapV(v,0)
    fcap_first = CapF(v,vn,0)
    objfile_str = ""
    objfile_str += "g cube\n"
    for i in v:
        for j in i:
            objfile_str += "v "+str(j[0])+" "+str(j[1])+" "+str(j[2])+"\n"
    for i in vn:
        for j in i:
            objfile_str += "vn "+str(j[0])+" "+str(j[1])+" "+str(j[2])+"\n"
    objfile_str += "vn "+str(vncap[0])+" "+str(vncap[1])+" "+str(vncap[2])+"\n"
    objfile_str += "vn "+str(vncap_first[0])+" "+str(vncap_first[1])+" "+str(vncap_first[2])+"\n"
    for i in f:
        for j in i:
            objfile_str += str(j)
    objfile_str += fcap
    objfile_str += fcap_first
    '''
    file=open("model2.obj","w")
    file.write("g cube\n")
    for i in v:
        for j in i:
            file.write("v "+str(j[0])+" "+str(j[1])+" "+str(j[2])+"\n")
    for i in vn:
        for j in i:
            file.write("vn "+str(j[0])+" "+str(j[1])+" "+str(j[2])+"\n")
    file.write("vn "+str(vncap[0])+" "+str(vncap[1])+" "+str(vncap[2])+"\n")
    file.write("vn "+str(vncap_first[0])+" "+str(vncap_first[1])+" "+str(vncap_first[2])+"\n")
    for i in f:
        for j in i:
            file.write(j)
    file.write(fcap)
    file.write(fcap_first)
    file.close()
    '''
    return objfile_str
