# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from profiles_api import models
from profiles_api import permissions

# Create your views here.
class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer
    """Test API view"""
    def get(self,request,format=None):
        """Return a list of APIView function"""
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'is similar to a traditional Django view',
        'Gives you the most control over the application logic',
        'Its manually mapped to a URL',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """ create a hello response with the name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message='Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,pk=None):
         """Handling updating object"""
         return Response({'method':'PUT'})
    def patch(self,request,pk=None):
         """Handle a partial update of an object"""
         return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
         """Delete an object"""
         return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API view set"""
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        """Return a hello message"""
        a_view_set=['User actions (list,craete,update and partial udate)',
        'Automatic maps URLS with reuter',
        'provide more functionality with less code'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
    def create(self,request):
        """Create a Hello Message"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valiid():
            name=serializer.validated_data('name')
            message='Hello {}!'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """"Handle an object with ID"""
        return Response({'http_method':'GET'})
    def update(self,request,pk=None):
        """Handle Updating an object with ID"""
        return Response({'http_method':"PUT"})
    def partial_update(self,request,pk=None):
        """Handle Updating part of an object ID"""
        return Response({'http_method':"PATCH"})
    def destroy(self,request,pk=None):
        """Handle removing an object ID"""
        return Response({'http_method':"DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating or updating the proile"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)
class UserLoginApiView(ObtainAuthToken):
    """creating user authentication token"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Hanles craeting reading and updating profile feed items"""
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(
        permissions.UpdateOwnStatus,
        IsAuthenticated,

    )


    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
