from rest_framework import serializers
from .models import Task,User
from django.contrib.auth import get_user_model

class TaskSerializer(serializers.ModelSerializer):
     by_person = serializers.ReadOnlyField(source='by_person.username')
     class Meta:
         model = Task
         fields = ('id','task_name','task_desc','completed','date_created','by_person')

class UserSerializer(serializers.ModelSerializer):
     #Task = serializers.PrimaryKeyRelatedField(many=True, queryset = Task.objects.all())
     password = serializers.CharField(write_only=True)


     def create(self, validated_data):
         user = get_user_model().objects.create(username = validated_data['username'])
         user.set_password(validated_data['password'])
         usr = User.objects.create(username = validated_data['username'])
         #user.password
         user.save()
         return user

     class Meta:
         model = User
         fields = ('first_name','last_name','email','username','password')



