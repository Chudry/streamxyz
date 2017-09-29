from django.contrib import admin

from .models import CollectionModel, CollectionItemModel


class CollectionItemInline(admin.StackedInline):
    model = CollectionItemModel
    readonly_fields = ('author', 'order_index')
    extra = 2


@admin.register(CollectionModel)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )
    inlines = [CollectionItemInline]
    readonly_fields = ('author', )

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, CollectionItemModel):
                instance.author = request.user
            instance.save()

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(CollectionAdmin, self).save_model(request, obj, form, change)


@admin.register(CollectionItemModel)
class CollectionItemAdmin(admin.ModelAdmin):
    list_display = ('collection', 'title', 'author', )
    readonly_fields = ('author', 'order_index')
