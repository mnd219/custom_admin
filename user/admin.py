from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BasUserAdmin
from user.models import User

# Register your models here.


class UserAdmin(BasUserAdmin):
    ordering = ['email']
    list_display = ['username', 'email', 'is_active', 'permission']
    list_filter = ['permission']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
