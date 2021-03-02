from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import formset_factory



class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('body',)


class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('body',)


class AddCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)
		widgets = {
			'body': forms.Textarea(attrs={'class':'form-control'})
		}
		error_messages = {
			'body':{
				'required': 'این فیلد اجباری است',
			}
		}
		help_texts = {
			'body':'max 400 char'
		}

class AddReplyForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)