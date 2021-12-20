from django.contrib import admin
from django.urls import path
from .views import RegisterView,LoginView,AccountView,LogoutView,LoginSimple,getUserID

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('account', AccountView.as_view()),
    path('logout', LogoutView.as_view()),
    path('simple', LoginSimple.as_view()),
    path('getid', getUserID.as_view()),
    
]