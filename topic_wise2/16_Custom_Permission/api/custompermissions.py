from rest_framework.permissions import BasePermission

# Creating a custom permission


class MyPermission(BasePermission):
    # We have to implement one method from these two method
    # 1. 'has_permission'
    # 2. 'has_object_permission'
    def has_permission(self, request, view):
        # we will give permission if request method is GET
        if request.method == 'POST':
            # return True will given permission to access
            return True

        # return False will not given permission to access
        return False

    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)
