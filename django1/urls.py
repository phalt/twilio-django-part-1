# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^sms/$', 'django1.views.sms'),
    url(r'^ring/$', 'django1.views.ring'),
)
