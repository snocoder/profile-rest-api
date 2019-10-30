from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets  #viewset

from profiles_api import serializers


class HelloApiView(APIView):
    """APIView testing"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Hello!! ',
            'snocoder',
        ]
        return Response({'message': 'I am from APIView', 'an_apiview': an_apiview})

    def post(self, request):
        """create hello mssg with name"""
        print(request.data)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


#viewset
class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        a_viewset = [
            'this is ',
            'viewset',
        ]
        return Response({'message':'hello!!', 'a_viewset': a_viewset})
