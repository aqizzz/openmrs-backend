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
        exclude = ['person']
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        person = Person.objects.create(gender='')
        person.save()
        
        validated_data['person'] = person
        

        user = Users.objects.create_user(
            email=email,
            password=password,
            **validated_data
        )

        return user

