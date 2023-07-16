
from django.shortcuts import render
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    permission_classes=[IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [IsAuthenticated] 
