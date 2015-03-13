from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import redirect

from votes_ensimag import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'votes_ensimag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', lambda r : redirect('votes/')),
    url(r'^votes/', include('votes.urls', namespace='votes')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

admin.site.site_header = 'Votes campagne Ensimag'
admin.site.site_title = 'Votes campagne Ensimag'
