from django.contrib import admin

from .models import Post, Like, UserProfile


@admin.register(UserProfile)
class UserProfileInline(admin.ModelAdmin):
    list_display = ('user', 'last_activity')
    readonly_fields = ('last_activity', )
    list_select_related = ('user', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at', 'id')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_select_related = (
        'post', 'user'
    )
    list_display = ('post', 'user', 'created_at')

