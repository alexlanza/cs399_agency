from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'agency.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)