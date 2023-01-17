from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:theme_id>', views.test_view, name="test_view"),
]