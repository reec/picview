from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'picview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'picview.views.index', name='index'),
    url(r'^(?P<slug>[^/]+)$', 'picview.views.album', name='album'),
    url(r'^(?P<slug>[^/]+)/(?P<position>\d+)$', 'picview.views.image', name='image'),
    url(
        r'^(?P<slug>[^/]+)/(?P<position>\d+)/image$',
        'picview.views.output_image',
        name    = 'output_image'
    ),
    url(
        r'^(?P<slug>[^/]+)/(?P<position>\d+)/thumbnail$',
        'picview.views.output_image_thumbnail',
        name    = 'output_image_thumbnail'
    ),
    url(r'^admin/', include(admin.site.urls)),
)
