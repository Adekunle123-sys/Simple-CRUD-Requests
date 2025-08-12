from crud.models import Item
from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    date_created = serializers.DateTimeField(read_only=True)
    author = serializers.SerializerMethodField()
    status = serializers.IntegerField()
    
    def get_author(self, obj):
        return obj.author.firstname
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return Item.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance