from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('placeorder/', views.placeorder),
    path('orders/', views.orders),
    path('cancel/<int:orderid>/', views.cancel),
    path('shopclose/', views.shopclose),
    path('profile/', views.profile)
]
