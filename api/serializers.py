from rest_framework import serializers
from django.contrib.auth.models import User
from content.models import Entry


class UserProfileSerializer(serializers.ModelSerializer):
    """Creating user and updating"""
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        """Updating the profile."""
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance


class UserDataSerializer(serializers.ModelSerializer):
    """A serializer for profile entry item."""
    class Meta:
        model = Entry
        fields = ['id', 'url', 'author', 'title', 'text', 'date_posted']
        extra_kwargs = {'author': {'read_only': True}}
