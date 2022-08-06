from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # now here we will define our custom permission
    def has_permission(self, request, view):
        # here we will return true or false

        # we will check is user is staff or not
        user = request.user
        if request.user.is_staff:
            return True
        print(user.get_all_permissions())
        return False

    # def has_object_permission(self, request, view, obj):
    #     return True
