from rest_framework.permissions import BasePermission,  SAFE_METHODS


class IsAuthor(BasePermission):
    message = 'You must be the author'
    print(message)
    def has_object_permissions(self,request,view,obj):
        print(obj)
        print(view)
        print(request.method)
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
