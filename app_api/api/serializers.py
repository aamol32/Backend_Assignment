from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from app_api.models import Post_detail,Follower

class RegistrationSerializer(serializers.ModelSerializer):
    password2 =serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwrgs ={
            'password': {'write_only':True}
        }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_detail
        fields = "__all__"

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = "__all__"
