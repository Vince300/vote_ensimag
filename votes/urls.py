from django.conf.urls import patterns, include, url
from votes import views

from votes_ensimag import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'votes_ensimag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^bulletin/$', views.bulletin, name='bulletin'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/votes'}, name='logout'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
