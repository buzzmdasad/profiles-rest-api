# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
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
