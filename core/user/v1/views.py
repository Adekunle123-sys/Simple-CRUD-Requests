from rest_framework import viewsets
from .serializers import UserSerializer
from user.models import User
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsUserOrAdmin

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAdminUser])
    def list_users(self, request):
        users = User.objects.all()
        serializer = self.get_serializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'], permission_classes=[IsUserOrAdmin])
    def get_item(self, request, pk=None):
        item = User.objects.all(pk=pk)
        serializer = self.get_serializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'], permission_classes=[IsAdminUser])
    def delete_item(self, request, pk=None):
        item = User.objects.all(pk=pk)
        serializer = self.get_serializer(item)
        serializer.delete()
        return Response(status=status.HTTP_200_OK)