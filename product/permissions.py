from rest_framework.permissions import BasePermission

from user.config import RoleChoices


class AdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == RoleChoices.ADMIN.value
        )


class AdminOrManagerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [
            RoleChoices.ADMIN.value,
            RoleChoices.MANAGER.value,
        ]
