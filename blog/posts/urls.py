from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^comments$', views.commentsReplys),
    url(r'^addcomment$', views.addComment),
    url(r'^$', views.showPosts),
]

urlpatterns += staticfiles_urlpatterns()