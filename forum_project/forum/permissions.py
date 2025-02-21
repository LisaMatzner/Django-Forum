from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Others can only read (GET).
    """

    def has_permission(self, request, view): # for list view
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser: 
            return True
        # print(obj.author)
        # print(request.user)
        # Write permissions are only allowed to the owner of the thread
        return obj.author == request.user