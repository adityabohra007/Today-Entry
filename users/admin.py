from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser


from .models import Post
admin.site.register(Post)


class CustomUserAdmin(UserAdmin):
	add_form=CustomUserCreationForm
	form=CustomUserChangeForm
	model=CustomUser
	lsit_display=['email','username','name']
admin.site.register(CustomUser,CustomUserAdmin)	