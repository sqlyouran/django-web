from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
import xadmin

xadmin.autodiscover()

urlpatterns = patterns('',
                       url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
                       url(r'^ueditor/', include('DjangoUeditor.urls' )),
                       )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)