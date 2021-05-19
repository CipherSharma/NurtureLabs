from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Advisor
from .models import Bookings

from rest_framework.serializers import ModelSerializer, ReadOnlyField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data.update({'id': self.user.id})
        return data
    @classmethod
    def get_token(cls, user):
        email = serializers.EmailField(label=("Email"))
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['id'] = user.id
        return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])


    class Meta:
        model = User
        fields = ('username', 'password', 'email')


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','email','password')

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bookings
        fields= '__all__'

class BookingsDisplaySerializer(serializers.ModelSerializer):
    Advisors = AdvisorSerializer(many=True,read_only=True)
    class Meta:
        model= Bookings
        fields= ('id','AdvisorId','Advisors','BookingTime')

