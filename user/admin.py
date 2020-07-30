from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class UserInline(admin.StackedInline):
    model = profiles
    can_delete = False
    verbose_name_plural = 'information'


class UserAdmin(UserAdmin):
    inlines = (UserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)