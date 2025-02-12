from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.patients.models.users import Users

class SankofiaTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    token['username'] = user.username
    token['email'] = user.email

    return token

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = '__all__'

