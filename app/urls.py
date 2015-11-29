# -*- coding: utf-8 -*- vim: set et ts=4 sw=4 :

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app.views import *

urlpatterns = patterns('',
    url(r'^$',MainView.as_view(), name='index'),
    url(r'^boobs_blender/$',Boobs_BlenderView.as_view(), name='boobs_blender'),
    url(r'^update/$','app.views.update_3D_object', name='update'),
    url(r'^makeBlender/$','app.views.executeBlender', name='makeBlender'),
#    url(r'^$','IGAView.as_view()', name = 'iga'),
#    url(r'^$','Boobs_BlenderView.as_view()', name = 'boobs_blender'),
)
