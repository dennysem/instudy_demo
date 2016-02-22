from django.contrib.auth.models import User
from restapi.models import Task
from rest_framework import viewsets
from restapi.serializers import UserSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
