from django.urls import path

from . import views


app_name = "blog"

urlpatterns = [
    path('viewposts/', views.posts_view, name='postview'),
    path('createpost/', views.post_create, name='postcreate'),
    ]