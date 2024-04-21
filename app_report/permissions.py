from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_object_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user.is_authenticated() and request.user
