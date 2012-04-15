from django.conf.urls import patterns, include, url

urlpatterns = patterns('ldnrealtime.tw.views',
    url(r'^echo$', 'echo', name='echo'),
    url(r'^record$', 'record', name='record'),
    url(r'^conference$', 'conference', name='conference'),
)
