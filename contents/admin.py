from django.contrib import admin
from .models import Content
from .models import Image
# from .models import FollowRelation


class ImageInline(admin.TabularInline):
    model = Image


class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = {'user', 'create_at'}


admin.register(Content, ContentAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass
