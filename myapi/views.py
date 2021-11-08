from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myapi.serializer import UserSerializer, GroupSerializer
from rest_framework import permissions

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API that allows user to view & edited
    """
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API that allows group to view & edited
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    