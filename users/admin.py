# from django.contrib import admin
# from django.contrib import auth
# from django.contrib.auth import admin as auth_admin
# from .forms import UserChangeForm, UserCreationForm

# from .models import User

# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     model = User

from django.db import models
from recruiters.models import Job
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
     
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('recruiter', 'title', 'compulsory_school')