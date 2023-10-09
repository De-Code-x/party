from django.contrib import admin
from .models import DecodeXCred
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountInLine(admin.StackedInline):
    model = DecodeXCred
    can_delete = False
    verbose_name_plural = "AdditionalUserCredential"

class CustomUserAdmin(UserAdmin):
    inlines = (AccountInLine, )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(DecodeXCred)