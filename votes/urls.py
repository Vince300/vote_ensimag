from django.conf.urls import patterns, include, url
from django.views.static import serve as serve_static
from django.contrib.auth.views import login as view_login, logout as view_logout
from votes import views

from votes_ensimag import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'votes_ensimag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', views.termine, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^bulletin/$', views.bulletin, name='bulletin'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', view_login, name='login'),
    url(r'^logout/$', view_logout, {'next_page': '/votes'}, name='logout'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [ url(r'^media/(?P<path>.*)$', serve_static, { 'document_root': settings.MEDIA_ROOT }) ]
