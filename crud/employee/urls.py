from django.urls import path
from .views import index, signin, signup, logout_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('login', signin, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout_user, name='logout'),
]