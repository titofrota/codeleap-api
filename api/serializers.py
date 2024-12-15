from rest_framework import serializers
from api.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'created_datetime']


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def validate(self, attrs):
        if 'username' in attrs:
            raise serializers.ValidationError({'username': 'This field cannot be updated.'})
        return attrs
