from django.urls import path,include
# from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('' , include('django.contrib.auth.urls')),
    path('signup/', views.signup, name = 'signup'),
    path('user/', views.user , name = 'user')
]
