from django.urls import path
from . import views
urlpatterns = [
    path('', views.accounts),
    path('otp/', views.generateOpt),
    path('otpverification/', views.otpverification),
    path('logout/', views.signout)
]
