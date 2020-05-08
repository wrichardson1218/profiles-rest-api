from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similiar to a tradational django view',
            'Gives you the most control over your application logic',
            'Is mapped mannually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})