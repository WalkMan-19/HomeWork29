from rest_framework.permissions import BasePermission


class AdCreatePermission(BasePermission):
    message = 'you are not the owner'

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin' or 'moderator':
            return True
        return False
