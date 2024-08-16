from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit owns profile"""
    def has_object_permission(self,request,view,obj):
        """User is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """allow to ad his own feed"""
    def has_object_permission(self,request,view,obj):
        """check user is trying to his own ststus"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id==request.user.id
