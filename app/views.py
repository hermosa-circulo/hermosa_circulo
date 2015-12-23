# -*- coding: utf-8 -*- vim: set et ts=4 sw=4 :
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os
import commands
from app.utils.Cylinder import makeobj
#from app.utils.bb import Lattice
class MainView(TemplateView):
    template_name = "index.html"
    def index(request):
        pass

class Boobs_BlenderView(TemplateView):
    template_name = "boobs_blender.html"
    def boobs_blender(request):
        pass

#3Dモデルの更新用
def update_3D_object(request):
    wheel_radius    =int(request.POST.get("wheel_radius",0))
    begining_point  = int(request.POST.get("begining_point",0))
    begin           = 100 - int(request.POST.get("begin",0))
    point_num       = int(request.POST.get("point_num",0))
    breast_wide     = 1.0 - float(request.POST.get("breast_wide",0.0))

    ret = makeobj.make(wheel_radius,begining_point,begin,point_num,breast_wide)
    file = open(os.path.join(os.getcwd(),'app/static/OBJfile/model2.obj'),'w')
    file.write(ret)
    file.close()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse(ret)

def executeBlender(request):
    wheel_radius    = request.POST.get("wheel_radius",0)
    begin           = request.POST.get("begin",0)
    point_num       = request.POST.get("point_num",0)
    breast_wide     = request.POST.get("breast_wide",0.0)

    currentdir = os.getcwd()
    strcommand = "blender --background --python %s /app/utils/bb/Lattice.py %s %s %s"%(currentdir, wheel_radius, begin,point_num, breast_wide)
    check = commands.getoutput(strcommand)

    #check = commands.getoutput("blender --background --python "check + "app/util/bb/Lattice.py 1 1 1 1")
    return HttpResponseRedirect(reverse('boobs_blender'))


'''
使ってないクラス
'''
class IGAView(TemplateView):
    template_name = "iga.html"
    def iga(request):
        pass
