from django.shortcuts import render
from django.views import generic
from django.http import Http404

from .models import *




def PostsView(request):
    try:
        p = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/posts.html', {'posts': p})

