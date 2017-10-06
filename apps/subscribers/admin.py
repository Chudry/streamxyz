from django.contrib import admin

from .models import SubscriberModel


@admin.register(SubscriberModel)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'interest', )
