from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.showPosts, name = 'home'),
    url(r'^(?P<post_id>[\w]+)$', views.showOnePost),
    url(r'^comment/$', views.addComment),
    url(r'^reply/$', views.addReply),
    url(r'^like/$', views.addLike),
    url(r'^Category/addPost$', views.addPost),
    url(r'^Category/(?P<cat_num>[\w]+)$', views.allCategoryPosts),
    url(r'^Search/$', views.searchForPost),
    url(r'^adminForbWords/$', views.adminForbWords),
    url(r'^adminForbWords/del/(?P<word_num>[\w]+)$', views.deleteWords),
    url(r'^adminForbWords/edit/(?P<word_num>[\w]+)$', views.editWords),
]

urlpatterns += staticfiles_urlpatterns()