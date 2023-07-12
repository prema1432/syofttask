from rest_framework.permissions import BasePermission

class AdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class AdminOrManagerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'manager']
