from django.contrib import admin
from api.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'title', 'created_datetime')
    search_fields = ('username', 'title')
    list_filter = ('created_datetime',)


admin.site.register(Post, PostAdmin)
