from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # now here we will define our custom permission
    # def has_permission(self, request, view):
    #     # here we will return true or false

    #     # we will check is user is staff or not
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.view_product"):
    #             # ("<app_name>.<verb_<model_name>>")
    #             # so here we are only giving access to those user who have permission to view_product
    #             return True
    #         if user.has_perm("products.change_product"):
    #             # if request user have permission to change then we are giving access to APIView
    #             return True
    #         if user.has_perm("products.add_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         return False
    #     return False
    # NOTE: this above permission will allow all the permission if user have only one of the permission

    # so to only allow specific permission for the requested user we will augment the permission as below

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        # we had added this part from the default permission
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # because we have added 'IsAdminUser' as permission on View itself we don't need to add this in here
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False

    #     # returning default permission
    #     return super().has_permission(request, view)

    # def has_object_permission(self, request, view, obj):
    #     return True
