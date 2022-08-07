from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    # now here we will create mixin class and create 'permission_class' which we want to use throughout the app
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

# Now we have permission mixin we can use it on any view that need it
