from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ('id', 'task_name', 'description', 'owner',
                  'task_date', 'status', 'created', 'modified',)
        read_only_fields = ('created', 'modified')


class UserSerializer(serializers.ModelSerializer):

    tasks = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks')
