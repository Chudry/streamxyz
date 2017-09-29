from django.contrib import admin

from .models import StreamModel, StreamItemModel


@admin.register(StreamModel)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )


@admin.register(StreamItemModel)
class StreamItemAdmin(admin.ModelAdmin):
    list_display = ('stream', 'title', 'author', )
