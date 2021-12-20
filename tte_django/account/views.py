from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from django.contrib import auth
from .serializers import LoginSerializer, UserSerializer
from .models import Account
import jwt, datetime
from django.conf import settings
from rest_framework import status

class RegisterView(APIView):
    authentication_classes=[]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    authentication_classes=[]
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Account.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        key='bisadonk'
        token = jwt.encode(payload, key, algorithm='HS256')
        
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class AccountView(APIView):
    authentication_classes=[]
    def post(self, request):
        
        # token = request.COOKIES.get('jwt')
        token = request.data['jwt']
        # test='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZXhwIjoxNjM1Njc2ODMxLCJpYXQiOjE2MzU2NzMyMzF9.TKdn6z7QmDOwkyZhUIchXE1yNWUaQUiA0KYW1hnzh8s'
        key='bisadonk'
        
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload=jwt.decode(token, key, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = Account.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'log out success'
        }
        return response

class LoginSimple(GenericAPIView):
    authentication_classes=[]

    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        key='bisadonk'
        user = auth.authenticate(username=email, password=password)

        if user:
            auth_token = jwt.encode(
                {'email': user.email}, key, algorithm="HS256")

            serializer = LoginSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class getUserID(APIView):
    authentication_classes=[]
    
    def post(self,request):
        email = request.data['email']
        user = Account.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        return Response({"id":user.id,"name":user.first_name+" "+user.last_name})