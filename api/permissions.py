from rest_framework import permissions


class IsAuthenticatedAndReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            # default deny is user can't be found
            return False
        if request.method in permissions.SAFE_METHODS:
            # read allowed for any authenticated user
            return request.user.is_authenticated
        else:
            # write not allowed
            return False


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            # default deny is user can't be found
            return False
        if request.method in permissions.SAFE_METHODS:
            # read allowed for any authenticated user
            return request.user.is_authenticated
        else:
            # write allowed for staff (see Django user model)
            return request.user.is_staff


class IsAdminOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            # default deny is user can't be found
            return False
        if request.method in permissions.SAFE_METHODS:
            # read allowed for any authenticated user
            return request.user.is_authenticated
        else:
            # write allowed for staff (see Django user model)
            return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # if not request.user:
        #     # default deny is user can't be found
        #     return False
        if request.method in permissions.SAFE_METHODS:
            # read allowed for any authenticated user
            return request.user.is_authenticated
        else:
            # write allowed for user who created the object
            return obj.user == request.user
