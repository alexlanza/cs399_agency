from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'agency.views.home', name='home'),
    url(r'^about/', 'agency.views.about', name='about'),
    url(r'^poll/', 'agency.views.about', name='poll'),
    url(r'^campaigns', 'agency.views.campaigns', name='campaigns'),
    url(r'^campaigns/mp3$', 'agency.views.mp3', name='mp3'),
    url(r'^campaigns/poll$', 'agency.views.poll', name='poll'),
    url(r'^email$', 'agency.views.email', name='email'),
    url(r'^admin/', include(admin.site.urls)),
)
