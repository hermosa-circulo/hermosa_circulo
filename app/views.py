# -*- coding: utf-8 -*- vim: set et ts=4 sw=4 :
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os
import commands
import random
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

class IGAView(TemplateView):
	template_name = "IGA.html"
	def IGA(request):
		pass

def update_3D_object(request):
    '''
    3Dモデルの更新用
    '''
    wheel_radius    = int(request.POST.get("wheel_radius",0))
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

    currentdir = str(os.getcwd())
    strcommand = "blender --background --python "+currentdir+"/app/utils/bb/Lattice.py "+wheel_radius+" "+begin+" "+point_num+" "+breast_wide
    check = commands.getoutput(strcommand)

    return HttpResponseRedirect(reverse('boobs_blender'))

def executeIGA(request):
	file_num = 3
	para_num = 5
	parameter=[[0 for i in range(para_num)] for j in range(file_num)]
	for i in range(len(parameter)):
		for j in range(len(parameter[0])):
			if j == 1:
				parameter[i][j] = 10
			elif j == 3:
				parameter[i][j] = 30
			elif j == 4:
				parameter[i][j] = random.uniform(0.15,0.6)
			else:
				parameter[i][j] = random.randint(30,70)

	for i in range(len(parameter)):
		ret = makeobj.make(parameter[i][0],parameter[i][1],parameter[i][2],parameter[i][3],parameter[i][4])
		file = open(os.path.join(os.getcwd(),'app/static/OBJfile/iga/iga'+str(i)+'.obj'),'w')
		file.write(ret)
		file.close()
	return HttpResponseRedirect(reverse('IGA'))
