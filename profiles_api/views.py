from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """APIView testing"""
    def get(self, request, format=None):
        an_apiview = [
            'Hello!! ',
            'snocoder',
        ]
        return Response({'message': 'I am from APIView', 'an_apiview': an_apiview})
