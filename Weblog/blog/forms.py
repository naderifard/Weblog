from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import formset_factory


class PostForm(forms.Form):
    caption = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField()
