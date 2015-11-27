# -*- coding: utf-8 -*- vim: set et ts=4 sw=4 :
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os
<<<<<<< HEAD
from app.utils.Closoid import makeobj
#from app.static.Closoid import makeobj
=======

#objファイル更新用のライブラリ
from app.utils import makeobj
>>>>>>> 0db24471301dba786f358936912aa4c4cb0e5f2b

#index.htmlを表示するだけのTemplateViewクラス
class MainView(TemplateView):
    template_name = "index.html"
    def hogehoge(request):
        pass

#3Dモデルの更新用
def update_3D_object(request):
    wheel_radius    = int(request.POST.get("wheel_radius",0))
    begining_point  = int(request.POST.get("begining_point",0))
    begin           = 100 - int(request.POST.get("begin",0))
    point_num       = int(request.POST.get("point_num",0))
    breast_wide     = 1.0 - float(request.POST.get("breast_wide",0.0))

    #objファイルの更新
    ret = makeobj.make(wheel_radius,begining_point,begin,point_num,breast_wide)
<<<<<<< HEAD
    #file = open(os.path.join(os.getcwd(),'app/static/Closoid/model2.obj'),'w')
    file = open(os.path.join(os.getcwd(),'app/static/OBJfile/model2.obj'),'w')
=======
    file = open(os.path.join(os.getcwd(),'app/static/model2.obj'),'w')
>>>>>>> 0db24471301dba786f358936912aa4c4cb0e5f2b
    file.write(ret)
    file.close()

    #indexページにリダイレクト
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse(ret)


'''
使ってないクラス
'''
class IGAView(TemplateView):
    template_name = "iga.html"
    def iga(request):
        pass

class Boobs_BlenderView(TemplateView):
    template_name = "boobs_blender.html"
    def boobs_blender(request):
        pass
