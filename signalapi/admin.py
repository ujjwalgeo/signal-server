from django.contrib import admin
from signalapi.models import SignalDocBase, Category


class SignalDocBaseAdmin(admin.ModelAdmin):
    model = SignalDocBase


class CategoryAdmin(admin.ModelAdmin):
    model = Category


admin.site.register(SignalDocBase, SignalDocBaseAdmin)
admin.site.register(Category, CategoryAdmin)
