from rest_framework.permissions import BasePermission, DjangoModelPermissions


class FullDjangoModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class IsWatchMember(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method == "GET":
                return request.user.groups.filter(name="Viewers").exists()
            elif request.method == "POST":
                return request.user.groups.filter(name="Editors").exists()
        return False
