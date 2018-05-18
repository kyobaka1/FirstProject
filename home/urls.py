from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login ,{'template_name':'pages/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout ,{'template_name':'pages/index.html'}, name='logout'),
    url(r'^upload/$', views.upLoad  , name='upload'),
    url(r'^check/$', views.check  , name='checkkey'),
    url(r'^buymusic/(?P<id>\d+)/$', views.buyMusic, name='buymusic'),
    url(r'^dowload/(?P<path>.*)/$', views.download, name='dowload'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)