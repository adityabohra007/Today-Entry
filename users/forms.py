from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser,Post
from django.utils import timezone
class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model=CustomUser
		fields=('username','email')
class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model=CustomUser
		fields=UserChangeForm.Meta.fields		



class PostForm(forms.ModelForm):
	Title=forms.CharField()
	Category=forms.CharField()
	Content=forms.CharField()
	Private=forms.CharField()
	class Meta:
		model = Post
		fields = ['Title','Category','Content','Private',]
    
