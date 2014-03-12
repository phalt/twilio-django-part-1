from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #Here we add our Twilio URLs
    url(r'^sms/$', 'django1.views.sms'),
    url(r'^ring/$', 'django1.views.ring'),
)
