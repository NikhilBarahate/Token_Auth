from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from app1.models import Students
from app1.serializers import StudentSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# Create your views here.
class StudentsDetails(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAdminUser,]