from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ldnrealtime.views.home', name='home'),
    url(r'^_tw/', include('ldnrealtime.tw.urls', namespace='tw')),

    url(r'^admin/', include(admin.site.urls)),
)
