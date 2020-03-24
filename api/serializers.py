from rest_framework import serializers
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """A Serializer for our user profile objects."""
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            """Create and return a new user."""
            user = UserProfile(
                username=validated_data['username'],
                email=validated_data['email']
            )

            user.set_password(validated_data['password'])
            user.save()

            return user
