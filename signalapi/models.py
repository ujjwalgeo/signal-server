from django.db import models
from geonode.documents.models import Document
from geonode.people.models import GroupProfile


class Collection(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    group = models.ForeignKey(GroupProfile, null=True, blank=True, on_delete=models.SET_NULL)


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    parent = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    icon = models.CharField(max_length=100, blank=False, null=False)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class SignalDocBase(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    doc = models.ForeignKey(Document, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    chart_html = models.CharField(max_length=5000, blank=True, null=True)
    collection = models.ForeignKey(Collection, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

