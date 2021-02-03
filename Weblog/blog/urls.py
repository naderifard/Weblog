from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsView, name='postview'),
    ]