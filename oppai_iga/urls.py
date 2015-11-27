from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^boobs_designer/',include('app.urls')),
    #url(r'^boobs_blender/',include('app.urls')),
]

urlpatterns += staticfiles_urlpatterns()
