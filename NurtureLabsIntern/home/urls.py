from django.contrib import admin
from django.urls import path,include

from .views import LoginView
from .views import RegisterView
from .views import AdvisorRegister
from .views import UserAdvisorRegister
from home import views


urlpatterns = [
    path('api/',views.ApiOverview, name="Api_Overview"),

    path('api/admin/advisor/',AdvisorRegister.as_view(), name="AdvisorRegister"),

    path('api/user/register/', RegisterView.as_view(), name="UserRegister"),
    #path('register/', RegisterView.as_view(), name='auth_register'),

    path('api/user/login/', LoginView.as_view(), name='token_obtain_pair'),
     #path('user/login/', views.UserLogin, name=" UserLogin"),

    path('api/user/<int:pk>/advisor/', views.GetUserAdvisor, name='GetUserAdvisor'),
    #path('/user/<user.id>/advisor', views.GetUserAdvisor, name=" /user/<user-id>/advisor"),

    path('api/user/<int:user_id>/advisor/<int:advisor_id>/', UserAdvisorRegister.as_view(), name='UserAdvisorRegister'),
    #path('/user/<user-id>/advisor/<advisor-id>/', views.UserAdvisorRegister, name="/user/<user-id>/advisor/<advisor-id>/"),
    
    path('api/user/<int:user_id>/advisor/booking/', views.UserAdvisorBookings, name='UserAdvisorBookings'),
    #path('/user/<user-id>/advisor/booking/', views.UserAdvisorBookings, name="/user/<user-id>/advisor/booking/"),
]



#  /user/register/
#  /user/login/
#  /user/<user-id>/advisor
#  /user/<user-id>/advisor/<advisor-id>/
#  /user/<user-id>/advisor/booking/