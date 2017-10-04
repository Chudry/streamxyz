from django.contrib import admin

from django import forms
from ckeditor.widgets import CKEditorWidget


from .models import QuizModel, QuestionModel


class QuestionForm(forms.ModelForm):
    question = forms.CharField(widget=CKEditorWidget())
    option_a = forms.CharField(widget=CKEditorWidget())
    option_b = forms.CharField(widget=CKEditorWidget())
    option_c = forms.CharField(widget=CKEditorWidget())
    option_d = forms.CharField(widget=CKEditorWidget())
    explanation = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = QuestionModel
        fields = '__all__'


class QuizForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = QuizModel
        fields = '__all__'


class QuestionInline(admin.StackedInline):
    model = QuestionModel
    form = QuestionForm
    readonly_fields = ('order_index', )
    extra = 5


@admin.register(QuizModel)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )
    inlines = [QuestionInline]
    readonly_fields = ('author', 'views', 'slug', )
    form = QuizForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(QuizAdmin, self).save_model(request, obj, form, change)


@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'order_index', )
    form = QuestionForm
