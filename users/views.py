from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer
from projects.models import Project  
from projects.serializers import ProjectSerializer


@api_view(['GET'])
def get_all(request):
    users = User.objects.all()
    if not users.exists():
        return Response({'message': 'No user found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    userSerializer = UserSerializer(data=request.data)
    if userSerializer.is_valid():
        user = userSerializer.save()
        fk_project = request.data.get('project_id')  
        project = Project.objects.get(id=fk_project)
        user.projects.add(project)

        return Response(userSerializer.data, status=status.HTTP_201_CREATED)
    return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user_and_project_by_id(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    projectSerializer = ProjectSerializer(project)
    userSerializer = UserSerializer(user)

    return Response({"user":userSerializer.data, "project": projectSerializer.data},status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get(request, pk):
    try:
        user = User.objects.get(id=pk)
        projects = user.projects.all()
        # Puedes personalizar la respuesta según tus necesidades
        serializerProject = ProjectSerializer(projects, many=True)
        userSerializer = UserSerializer(user)
        return Response({"user":userSerializer.data, "projects": serializerProject.data}, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
