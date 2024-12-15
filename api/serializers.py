from rest_framework import serializers
from api.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'created_datetime']

    def validate(self, attrs):
        if self.instance and 'username' in attrs:
            raise serializers.ValidationError('username field cannot be updated')
        return attrs
