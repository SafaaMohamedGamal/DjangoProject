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
    #================
    url(r'^subscribe/(?P<cat_num>[\w]+)$', views.subcribe),
    # url(r'^unsubscribe/(?P<cat_num>[1-3])$', views.unSubscribeCategory),
    url(r'^list/$', views.listPosts),
    url(r'^delpost/(?P<post_num>[\w]+)$', views.deletePost),
    url(r'^editpost/(?P<post_num>[\w]+)$', views.editPost),
    url(r'^addPost/$', views.addPost),
    url(r'^catlist/$', views.listCategories),
    url(r'^delcat/(?P<cat_num>[\w]+)$', views.deleteCategory),
    url(r'^editcat/(?P<cat_num>[\w]+)$', views.editCategory),
    url(r'^addcat/$', views.addCategory),

]

urlpatterns += staticfiles_urlpatterns()