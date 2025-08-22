from rest_framework import viewsets, serializers
from .serializers import ItemSerializer
from crud.models import Item
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user.v1.permissions import IsAdminOrReaOnly, IsUserOrAdmin
from rest_framework.permissions import IsAdminUser, AllowAny


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    # permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]           
        elif self.action in ["list"]:
            return [AllowAny()]  
        elif self.action in ["retrieve"]:
            return [IsUserOrAdmin()]       
        elif self.action in ["update", "partial_update"]:
            return [IsUserOrAdmin()]
        elif self.action in ["destroy"]:
            return [IsUserOrAdmin()]  
        return super().get_permissions()