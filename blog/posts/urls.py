from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^comments$', views.commentsReplys),
    url(r'^addcomment$', views.addComment),
    url(r'^Category/addPost$', views.addPost),
    url(r'^Category/(?P<cat_num>[1-3])$', views.allCategoryPosts),
    url(r'^$', views.showPosts),
    url(r'^Search/$', views.searchForPost),
]

urlpatterns += staticfiles_urlpatterns()