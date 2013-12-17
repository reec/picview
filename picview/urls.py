from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'picview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'picview.views.index', name='index'),
    url(r'^album/(?P<slug>[^/]+)$', 'picview.views.album', name='album'),
    url(r'^album/(?P<slug>[^/]+)/(?P<position>\d+)$', 'picview.views.image', name='image'),
    url(r'^admin/', include(admin.site.urls)),
)
