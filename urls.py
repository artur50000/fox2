
from django.urls import path, include
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    path('profedit', views.profedit, name='profedit'),
    path('add_image', views.add_image, name='add_image'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),  
    
   ]