from allauth.account.utils import user_field, user_email, user_username
from django.http import HttpResponse, Http404, JsonResponse
from geonode.api.authentication import OAuthAuthentication
import json


def user_info(request):
    is_authenticated = OAuthAuthentication().is_authenticated(request)

    if is_authenticated:
        user = request.user
        groups = [group.name for group in user.groups.all()]
        if user.is_superuser:
            groups.append("admin")

        user_info = json.dumps({
            "sub": str(user.id),
            "name": " ".join([user_field(user, 'first_name'), user_field(user, 'last_name')]),
            "given_name": user_field(user, 'first_name'),
            "family_name": user_field(user, 'last_name'),
            "email": user_email(user),
            "preferred_username": user_username(user),
            "groups": groups
        })

        response = HttpResponse(
            user_info,
            content_type="application/json"
        )
        response['Cache-Control'] = 'no-store'
        response['Pragma'] = 'no-cache'

        return response
    else:
        return HttpResponse(status=404)
