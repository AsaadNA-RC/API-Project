from rest_framework import serializers
from .models import UserData

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

'''
    Custom Claim for JWT Payload
'''

class CustomTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id', 'email', 'name', 'password']

    '''
        We want to be able to save data that is validated
        so we override create that will run on .save()
    '''

    def create(self, validated_data):
        user = UserData.objects.create(
            email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
