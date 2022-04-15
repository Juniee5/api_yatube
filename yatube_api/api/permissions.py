from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == r.user or r.method in permissions.SAFE_METHODS
