from tastypie.resources import ModelResource
from tastypie.fields import ForeignKey
from signalapi.models import SignalDocBase, Category
from geonode.api.authentication import OAuthAuthentication
from geonode.api.resourcebase_api import DocumentResource
import json
from django.core.serializers.json import DjangoJSONEncoder
from tastypie.serializers import Serializer


class SignalDocBaseResource(ModelResource):
    doc = ForeignKey(DocumentResource, "doc", full=True)

    class Meta:
        queryset = SignalDocBase.objects.all()
        resource_name = "signaldoc"
        authentication = OAuthAuthentication()


class CategoryResource(ModelResource):
    parent = ForeignKey("signalapi.api.CategoryResource", "parent", full=False, null=True)

    def dehydrate(self, bundle):
        bundle.data['parent_id'] = bundle.obj.parent_id
        return bundle

    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"
        authentication = OAuthAuthentication()
