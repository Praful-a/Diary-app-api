from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit thier own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class PostOwnEntry(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own entry."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.id == request.user.id
