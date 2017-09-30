from django.contrib import admin

from django import forms
from ckeditor.widgets import CKEditorWidget


from .models import CollectionModel, CollectionItemModel


class CollectionItemForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = CollectionItemModel
        fields = '__all__'


class CollectionForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = CollectionModel
        fields = '__all__'


class CollectionItemInline(admin.StackedInline):
    model = CollectionItemModel
    form = CollectionItemForm
    readonly_fields = ('author', )
    extra = 2


@admin.register(CollectionModel)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )
    inlines = [CollectionItemInline]
    readonly_fields = ('author', )
    form = CollectionForm

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
    readonly_fields = ('author', )
    form = CollectionItemForm
