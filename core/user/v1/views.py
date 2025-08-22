from rest_framework import viewsets
from .serializers import UserSerializer
from user.models import User
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsSelfOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]           
        elif self.action in ["list"]:
            return [AllowAny()]  
        elif self.action in ["retrieve"]:
            return [IsSelfOrAdmin()]       
        elif self.action in ["update", "partial_update"]:
            return [IsAdminUser()]
        elif self.action in ["destroy"]:
            return [IsAdminUser()]  
        return super().get_permissions()
