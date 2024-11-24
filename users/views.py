from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def get_all(request):
    users = User.objects.all()
    if not users.exists():
        return Response({'message': 'No user found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

