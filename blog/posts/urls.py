from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.commentsReplys),
]

urlpatterns += staticfiles_urlpatterns()