from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import News
from django.contrib import admin



User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_date')
    list_filter = ('news_date','news_title')

