from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.showPosts),
    url(r'^(?P<post_id>[\w]+)$', views.showOnePost),
    url(r'^comment/$', views.addComment),
    url(r'^reply/$', views.addReply),
    url(r'^like/$', views.addLike),
    url(r'^Category/addPost$', views.addPost),
    url(r'^Category/(?P<cat_num>[1-3])$', views.allCategoryPosts),
    url(r'^Search/$', views.searchForPost),
]

urlpatterns += staticfiles_urlpatterns()