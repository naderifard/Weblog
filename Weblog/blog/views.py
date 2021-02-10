from django.shortcuts import render
from django.views import generic
from django.http import Http404
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import SignUp
from django.shortcuts import render, redirect, reverse
from django.db import IntegrityError
from django.contrib.auth import login


def posts_view(request):
    try:
        p = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/postsview.html', {'posts': p})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            caption=form.cleaned_data['caption']
            tags=form.cleaned_data['tags']
            tags=tags.split()
            #author = get_object_or_404(User, username=request.user.username)
            post=Post.objects.create(caption=caption,user=request.user,pub_date=timezone.now())
            for i in tags:
                Tag.objects.create(post=post,text=i)
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'blog/postscreate.html', {'form': form})




def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'],
                                               password=request.POST['password'])
            login(request,user)

            return HttpResponseRedirect('/blog/viewposts/')

    else:
        form = SignUp()

    return render(request, 'blog/signup.html', {'form': form})

