from rest_framework import serializers
from api.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'username', 'title', 'content', 'created_datetime', 'updated_datetime')
        read_only_fields = ('created_datetime', 'updated_datetime')