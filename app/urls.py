from django.conf.urls import url,include
from django.contrib import admin

from . import views



urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^api/$', views.PostList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^co/$', views.CommentList.as_view()),
    url(r'^co/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    url(r'^addPost/$', views.add_post, name='add_post'),
    url(r'^$', views.PostListView.as_view(),name='home'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^editPost/(?P<slug>[\w-]+)/$', views.edit_post, name='edit_post'),
    url(r'^deletePost/(?P<slug>[\w-]+)/$', views.delete_post, name='delete_post'),
    url(r'^post_api/$', views.PostList.as_view),
    url(r'^co/$', views.CommentList.as_view()),
    url(r'^co/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),



    # url(r'^(?P<slug>[\w-]+)-(?P<id>[0-9]+)/$',views.detail, name='detail')
]
