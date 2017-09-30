from django.contrib import admin

from django import forms
from ckeditor.widgets import CKEditorWidget


from .models import StreamModel, StreamItemModel


class StreamItemForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = StreamItemModel
        fields = '__all__'


class StreamForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = StreamModel
        fields = '__all__'


class StreamItemInline(admin.StackedInline):
    model = StreamItemModel
    form = StreamItemForm
    readonly_fields = ('author', )
    extra = 2


@admin.register(StreamModel)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )
    inlines = [StreamItemInline]
    readonly_fields = ('author', )
    form = StreamForm

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, StreamItemModel):
                instance.author = request.user
            instance.save()

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(StreamAdmin, self).save_model(request, obj, form, change)


@admin.register(StreamItemModel)
class StreamItemAdmin(admin.ModelAdmin):
    list_display = ('stream', 'title', 'author', )
    readonly_fields = ('author', )
    form = StreamItemForm
