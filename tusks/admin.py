from django.contrib import admin
from .models import Tusks, Task_Comment, User_Tusks, Tag

# admin.site.register(Tusks)

# admin.site.register(User_Tusks)

@admin.register(User_Tusks)
class AdminTusks(admin.ModelAdmin):
    list_display = ('user_id', 'tusks_id')
    list_filter = ('user_id',)

@admin.register(Tusks)
class AdminTusks(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)

@admin.register(Task_Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('tusks_id', 'comment_date','text_comment')
    list_filter = ('tusks_id','comment_date')
    search_fields = ('comment_date', 'text_comment')
    readonly_fields = ('comment_date','text_comment')
    date_hierarchy = 'comment_date'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'name',
 
admin.site.site_header = "Моя административная панель"



