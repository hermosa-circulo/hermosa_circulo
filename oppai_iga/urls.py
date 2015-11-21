from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^boobs_designer/',include('app.urls')),
]

urlpatterns += staticfiles_urlpatterns()