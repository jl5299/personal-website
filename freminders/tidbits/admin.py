from django.contrib import admin
from .models import User, Friend, FriendNote

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(FriendNote)

# Register your models here.
