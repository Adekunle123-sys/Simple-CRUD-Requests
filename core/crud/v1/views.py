from rest_framework import viewsets, serializers
from .serializers import ItemSerializer
from crud.models import Item
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user.v1.permissions import IsAdminOrReaOnly, IsUserOrAdmin
from rest_framework.permissions import IsAdminUser

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    # permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['POST'], permission_classes = [IsAuthenticated], url_path='create')
    def create_item(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['GET'], permission_classes=[])
    def list_items(self, request):
        items = Item.objects.all()
        serializer = self.get_serializer(items)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'], permission_classes=[IsUserOrAdmin])
    def get_item(self, request, pk=None):
        item = Item.objects.all(pk=pk)
        serializer = self.get_serializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'], permission_classes=[IsAdminUser])
    def delete_item(self, request, pk=None):
        item = Item.objects.all(pk=pk)
        serializer = self.get_serializer(item)
        serializer.delete()
        return Response(status=status.HTTP_200_OK)
    
    