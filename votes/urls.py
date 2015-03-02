from django.conf.urls import patterns, include, url
from votes import views

from votes_ensimag import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'votes_ensimag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^(?P<liste_id>\d+)/$', views.detail, name='detail')
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
