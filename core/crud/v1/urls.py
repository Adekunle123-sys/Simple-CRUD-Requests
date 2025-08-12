from django.urls import path, include
from .views import ItemList, ItemDetail

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('item/<int:pk>/detail/', ItemDetail.as_view(), name='item-detail'),
]