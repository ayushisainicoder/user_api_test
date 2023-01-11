from django.shortcuts import render
from .models import CustomerUser
from . serializers import UserSerializer
from rest_framework import viewsets
# Create your views here.




class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer