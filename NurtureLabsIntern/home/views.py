from django.db.models.expressions import Value
from django.shortcuts import render
from django.http import JsonResponse
#JWT Response Tokens
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .serializers import AdvisorSerializer
from .serializers import BookingsSerializer
from .serializers import BookingsDisplaySerializer
from .models import Advisor, Bookings

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from .serializers import RegisterSerializer
from rest_framework import generics


# Create your views here.



@api_view(['GET'])
def ApiOverview(request):
    api_urls ={
        'AdvisorRegister:api/admin/advisor/',
        'UserRegister:api/user/register/',
        'UserLogin:api/user/login/',
        'GetUserAdvisor:api/user/<user-id>/advisor',
        'UserAdvisorRegister:api/user/<user-id>/advisor/<advisor-id>/',
        'UserAdvisorBookings:api/user/<user-id>/advisor/booking/',
    }
    return Response(api_urls)


class AdvisorRegister(APIView):
    parser_classes=[MultiPartParser,FormParser]
    def post(self,request,format=None):
        print (request.data)
        serializer=AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
#    {
#"username": "Cipher",
#"email" : "tudsharma@gmail.com",
#"password" : "Tushar@0380"
#}

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
  
    

@api_view(['GET'])
def GetUserAdvisor(request,pk=id):
    Advisors=Advisor.objects.all()
    serializer=AdvisorSerializer(Advisors,many=True)
    return Response(serializer.data)

class UserAdvisorRegister(CreateAPIView):
    serializer_class=BookingsSerializer
    def get(self,request,user_id,advisor_id):
        uid=user_id
        aid=advisor_id
        serializer = BookingsSerializer( data={'UserId': uid,'AdvisorId':aid}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,user_id,advisor_id,format=None):
        Booking=Bookings.objects.last()
        serializer=BookingsSerializer(Booking,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def UserAdvisorBookings(request,user_id):
    Booking=Bookings.objects.filter(UserId=user_id)
    serializer=BookingsDisplaySerializer(Booking,many=True)
    return Response(serializer.data)

    

