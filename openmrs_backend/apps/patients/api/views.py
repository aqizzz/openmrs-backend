from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.patients.api import serializers as api_serializer
from apps.patients.api.serializers import UsersSerializer
from apps.patients.models.users import Users

class SankofiaTokenObtainPairView(TokenObtainPairView):
  serializer_class = api_serializer.SankofiaTokenObtainPairSerializer

@api_view(['POST'])
def user_create(request):
  if request.method == 'POST':
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])  
def user_detail(request, id):
  try:
    user = Users.objects.get(user_id=id)
  except Users.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = UsersSerializer(user)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  if request.method == 'DELETE':
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)