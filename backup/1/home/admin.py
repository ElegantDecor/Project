from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'username','password','user_type')
    search_fields = ('name', 'email', 'username')

admin.site.register(Users, UsersAdmin)
