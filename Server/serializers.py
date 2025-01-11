from rest_framework import serializers
from django.contrib.auth.models import User

#For mapping json objects from apis to entries in database
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']