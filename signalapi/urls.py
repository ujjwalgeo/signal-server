from tastypie.api import Api
from . import api as resources
from django.conf.urls import url, include


api = Api(api_name='api')
api.register(resources.SignalDocBaseResource())
api.register(resources.CategoryResource())

urlpatterns = [
    url(r'^', include(api.urls)),
]
