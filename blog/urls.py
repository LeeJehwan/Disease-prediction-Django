from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^analysis/$', views.analysis, name='analysis'),
    url(r'^result/$', views.result, name='result'),
    url(r'^analysis/no_disease/$', views.no_disease, name='no_disease'),
    url(r'^analysis/has_disease/$', views.has_disease, name='has_disease'),
    url(r'^people/$', views.people, name='people'),
    url(r'^result2/$', views.result2, name='result2'),
]