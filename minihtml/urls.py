from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.post_new, name='post_new'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<slug>[^\.]+)/$', views.post_detail, name='post_detail'),

]