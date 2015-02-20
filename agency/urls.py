from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'agency.views.home', name='home'),
                       url(r'^about$', 'agency.views.about', name='about'),
                       url(r'^campaigns$', 'agency.views.campaigns', name='campaigns'),
                       url(r'^campaigns/mp3$', 'agency.views.mp3.mp3', name='mp3'),
                       url(r'^campaigns/mtndewpoll$', 'agency.views.mtndewpoll.mtndewpoll', name='mtndewpoll'),
                       url(r'^campaigns/email$', 'agency.views.email.email', name='email'),
                       url(r'^admin/', include(admin.site.urls)),
)
