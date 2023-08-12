from rest_framework.permissions import BasePermission


class IsAuthorOrAdmin(BasePermission):
    """Кастомный пермишн для админа или автора"""
    def has_object_permission(self, request, view, obj):
        return (obj.author.id == request.user.id or
                request.user.is_staff or request.user.is_superuser)
