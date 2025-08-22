from user.models import User
from crud.models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Item
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return super().create(validated_data)
        
    def get_user(self, obj):
        return obj.user.email