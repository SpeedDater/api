from rest_framework import permissions


class IsAdminOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            # default deny is user can't be found
            return False
        # write allowed if authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if not request.user:
            # default deny is user can't be found
            return False
        if request.method in permissions.SAFE_METHODS:
            # read allowed for any authenticated user
            return request.user.is_authenticated
        else:
            # write allowed for user who created the object or staff
            return obj.user == request.user or request.user.is_staff
