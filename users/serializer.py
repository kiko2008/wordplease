from django.contrib.auth.models import User
from rest_framework import serializers


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()


class UserSerializer(UserListSerializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, request_data):
        user = User()
        return self.update(user, request_data)

    def update(self, instance, request_data):
        if request_data.get('first_name') is not None:
            instance.first_name = request_data.get('first_name')

        if request_data.get('last_name') is not None:
            instance.last_name = request_data.get('last_name')

        if request_data.get('username') is not None:
            instance.username = request_data.get('username')

        if request_data.get('email') is not None:
            instance.email = request_data.get('email')

        if request_data.get('password') is not None:
            instance.set_password(request_data.get('password'))

        instance.save()
        return instance

    def validate_username(self, value):
        # for new users
        if self.instance is not None and self.instance.username != value and User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username {0} already exists'.format(value))

        # for update existing user
        if self.instance is None and User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username {0} already exists'.format(value))

        return value
