from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

        
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'forum.views.home'),
    url(r'^register/', 'forum.views.register'),
    url(r'^login/', 'forum.views.login'),
    url(r'^logout/', 'forum.views.logout'),

    url(r'^personal_page/', 'forum.views.personal_page'),

    url(r'^threads/$', 'forum.views.all_threads'),
    url(r'^threads/(.+)/$', 'forum.views.thread'),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
