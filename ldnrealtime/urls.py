from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ldnrealtime.views',
    url(r'^$', 'home', name='home'),
    url(r'^pusher/location', 'pusher_location', name='pusher_location'),
    url(r'^pusher/auth', 'pusher_auth', name='pusher_auth'),
    url(r'^_tw/', include('ldnrealtime.tw.urls', namespace='tw')),
    url(r'^admin/', include(admin.site.urls)),
)
