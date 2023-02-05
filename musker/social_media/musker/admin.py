from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Meep, Profile

admin.site.unregister(Group)


# Include Profile with User Info
class ProfileInline(admin.StackedInline):
    model = Profile
    list_display = ("username",)


# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


# unregister initial user
admin.site.unregister(User)

# Register new user
admin.site.register(User, UserAdmin)

# Register Profile
# admin.site.register(Profile)

admin.site.register(Meep)
