from django.contrib import admin
from signalapi.models import SignalDocBase, Category, Collection


class SignalDocBaseAdmin(admin.ModelAdmin):
    model = SignalDocBase


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class CollectionAdmin(admin.ModelAdmin):
    model = Collection


admin.site.register(SignalDocBase, SignalDocBaseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
