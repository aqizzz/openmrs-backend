from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.patients.models.users import Users
from apps.patients.models.person import Person

class SankofiaTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    token['username'] = user.username
    token['email'] = user.email

    return token

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__' 

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'person': {'required': False, 'read_only': True} 
        }
        
    def create(self, validated_data):

        user = Users.objects.create_user(
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )

        return user

