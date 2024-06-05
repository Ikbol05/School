from django.shortcuts import render
from rest_framework import viewsets
from .models import Class, Teacher, Student
from .serializers import ClassSerializer, TeacherSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.




class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]