from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login , logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
#from .models import Profile, Relation
from django.http import JsonResponse
from .forms import UserRegistrationForm,UserLoginForm,EditProfileForm
from blog.models import Post
from .models import Relation,Profile
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def user_login(request):
	next = request.GET.get('next')
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user is not None:
				login(request, user)
				messages.success(request, 'you logged in successfully', 'success')
				if next:
					return redirect(next)
				return redirect('blog:all_posts')
			else:
				messages.error(request, 'wrong username or password', 'warning')
	else:
		form = UserLoginForm()
	return render(request, 'accounts/login.html', {'form':form})

def user_register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
			login(request, user)
			messages.success(request, 'you registered successfully', 'success')
			return redirect('blog:all_posts')
	else:
		form = UserRegistrationForm()
	return render(request, 'accounts/register.html', {'form':form})


@login_required
def user_logout(request):
	logout(request)
	messages.success(request, 'you logged out successfully', 'success')
	return redirect('blog:all_posts')


@login_required
def user_dashboard(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	posts = Post.objects.filter(user=user)
	self_dash = False
	if request.user.id == user_id:
		self_dash = True
	return render(request, 'accounts/dashboard.html', {'user':user, 'posts':posts, 'self_dash':self_dash})

@login_required
def edit_profile(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=user.profile)
		if form.is_valid():
			form.save()
			user.email = form.cleaned_data['email']
			user.save()
			messages.success(request, 'your profile edited successfully', 'success')
			return redirect('accounts:dashboard', user_id)
	else:
		form = EditProfileForm(instance=user.profile, initial={'email':request.user.email})
	return render(request, 'accounts/edit_profile.html', {'form':form})