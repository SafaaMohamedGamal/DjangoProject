from django.urls import path,include
from . import views

urlpatterns = [
    path('' , views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
<<<<<<< HEAD
    # path('user/', views.user, name = 'user'),
    path('accounts/', include('django.contrib.auth.urls')),
    

=======
    path('accounts/', include('django.contrib.auth.urls'))
>>>>>>> 9c6f0cc3461e3f390de1f4726ae14b998e9fa3c0
]
