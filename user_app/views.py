from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def RegiaterView(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'User Register Successfully!'
            data['player_name'] = account.username
            data['email'] = account.email

            return Response(data)
        else:
            return Response(serializer.errors)