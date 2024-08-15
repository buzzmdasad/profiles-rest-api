# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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
