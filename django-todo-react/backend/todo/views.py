from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()




#fra: https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react#step-1-setting-up-the-backend