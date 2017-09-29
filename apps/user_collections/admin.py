from django.contrib import admin

from .models import CollectionModel, CollectionItemModel


@admin.register(CollectionModel)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )


@admin.register(CollectionItemModel)
class CollectionItemAdmin(admin.ModelAdmin):
    list_display = ('collection', 'title', 'author', )
