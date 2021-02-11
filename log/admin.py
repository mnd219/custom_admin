from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from log.models import User, Company

class UserAdminForm(UserChangeForm):

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
            'js/useradmin.js',
        )

class UserCreateForm(UserCreationForm):
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
            'js/useradmin.js',
        )


class UserAdmin(BaseUserAdmin):
    form = UserAdminForm
    add_form = UserCreateForm
    ordering = ['username']
    list_display = ['username', 'email', 'is_active', 'permission']
    list_filter = []
    fieldsets = ((None, {'fields': ('username', 'email', 'permission', 'companies')}),)
    filter_horizontal = ('companies',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'permission', 'companies')}
        ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Company)
admin.site.unregister(Group)
