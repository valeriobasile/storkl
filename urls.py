from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'storkl.views.home', name='home'),
    # url(r'^storkl/', include('storkl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard', 'storklapp.views.dashboard'),
    url(r'^project/(?P<project_id>\d+)$', 'storklapp.views.project'),
    url(r'^edit_project/(?P<project_id>\d+)$', 'storklapp.views.edit_project'),
    url(r'^delete_project/(?P<project_id>\d+)$', 'storklapp.views.delete_project'),
    url(r'^task/(?P<task_id>\d+)$', 'storklapp.views.task'),
    url(r'^delete_task/(?P<task_id>\d+)$', 'storklapp.views.delete_task'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'storklapp/login.html'}),
    url(r'^logout/$', 'storklapp.views.view_logout'),
)

if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
