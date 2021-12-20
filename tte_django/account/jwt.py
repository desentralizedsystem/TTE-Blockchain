
import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User

from account.models import Account


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        key='bisadonk'

        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, key, algorithms="HS256")

            user = Account.objects.get(email=payload['email'])
            return (user, token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired,login')

        return super().authenticate(request)