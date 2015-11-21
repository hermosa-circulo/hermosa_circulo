# -*- coding: utf-8 -*- vim: set et ts=4 sw=4 :
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    def index(request):
        pass



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
