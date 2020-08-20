from tastypie.resources import ModelResource
from tastypie.fields import ForeignKey
from signalapi.models import SignalDocBase, Category, Collection
from geonode.api.authentication import OAuthAuthentication
from geonode.api.resourcebase_api import DocumentResource
import json
from django.core.serializers.json import DjangoJSONEncoder
from tastypie.serializers import Serializer
from tastypie.constants import ALL


class CollectionResource(ModelResource):
    class Meta:
        queryset = Collection.objects.all()
        resource_name = "collection"
        authentication = OAuthAuthentication()
        filtering = {"group": ["exact"]}


class CategoryResource(ModelResource):
    parent = ForeignKey("signalapi.api.CategoryResource", "parent", full=False, null=True)

    def dehydrate(self, bundle):
        bundle.data['parent_id'] = bundle.obj.parent_id
        return bundle

    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"
        authentication = OAuthAuthentication()


class SignalDocBaseResource(ModelResource):
    doc = ForeignKey(DocumentResource, "doc", full=False)
    collection = ForeignKey(CollectionResource, "collection", full=True)
    category = ForeignKey(CategoryResource, "category", full=True)

    class Meta:
        queryset = SignalDocBase.objects.all()
        resource_name = "signaldoc"
        authentication = OAuthAuthentication()
        filtering = {"collection": ["exact"], "category": ALL}

