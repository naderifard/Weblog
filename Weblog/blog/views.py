from django.shortcuts import render
from django.views import generic
from django.http import Http404
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse
from django.db import IntegrityError
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.utils.text import slugify

def all_posts(request):
    try:
        p = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/allposts.html', {'posts': p})


def post_detail(request):
    def post_detail(request,year, month, day, slug):
        post = get_object_or_404(Post, created__year=year, created__month=month, created__day=day, slug=slug)
        comments = Comment.objects.filter(post=post, is_reply=False)
        reply_form = AddReplyForm()
        if request.method == 'POST':
            form = AddCommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post
                new_comment.user = request.user
                new_comment.save()
                messages.success(request, 'your comment submitted successfully')
        else:
            form = AddCommentForm()
        return render(request, 'blog/postdetail.html',
                      {'post': post, 'comments': comments, 'form': form, 'reply': reply_form})


def add_post(request,user_id):
    if request.user.id == user_id:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.slug = slugify(form.cleaned_data['body'][:30])
                new_post.save()
                messages.success(request, 'your post submitted', 'success')
                return redirect('accounts:dashboard', user_id)
        else:
            form = AddPostForm()
        return render(request, 'blog/postscreate.html', {'form': form})
    else:
        return redirect('blog:postview')


def post_delete(request):
    pass


def post_edit(request):
    pass







