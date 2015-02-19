from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'agency.views.home', name='home'),
    url(r'^about$', 'agency.views.about', name='about'),
    url(r'^campaigns$', 'agency.views.campaigns', name='campaigns'),
    url(r'^campaigns/mp3$', 'agency.views.mp3.mp3', name='mp3'),
    url(r'^campaigns/mtndewpoll/$', 'agency.views.mtndewpoll', name='mtndewpoll'),
    url(r'^campaigns/mtndewpoll/results/$', 'agency.views.mtndewpoll', name='results'),
    url(r'^campaigns/mtndewpoll$/vote/$', 'agency.views.mtndewpoll', name='vote'),
	url(r'^campaigns/email$', 'agency.views.email.email', name='email'),
    url(r'^admin/', include(admin.site.urls)),
)
