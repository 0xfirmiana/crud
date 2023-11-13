from django.urls import path
from .views import index, signin, signup, logout_user, add_employee, edit, delete, search
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('login', signin, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout_user, name='logout'),
    path('add', add_employee, name='add_employee'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('search/', search, name='search'),
]