from django.urls import include
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:theme_id>', views.test_view, name="test_view"),
    path('users', include('django.contrib.auth.urls')),
    path('users/login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(template_name='login/login.html'), name="logout")
]