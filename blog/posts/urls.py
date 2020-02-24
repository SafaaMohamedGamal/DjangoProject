from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^comments$', views.commentsReplys),
    url(r'^(?P<post_id>[\w]+)$', views.showOnePost),
    # url(r'^(?P<postid>[\w]+)/(?P<newComment>[\w]+)/$', views.addComment),
    url(r'^comment/$', views.addComment),
    url(r'^reply/$', views.addReply),
    url(r'^like/$', views.addLike),
    url(r'^$', views.showPosts),
]

urlpatterns += staticfiles_urlpatterns()