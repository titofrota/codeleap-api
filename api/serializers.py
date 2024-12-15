from rest_framework import serializers
from api.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'created_datetime']

    def validate(self, attrs):
        # During partial update, username cannot be updated
        if self.instance:
            if 'username' in attrs:
                raise serializers.ValidationError({'username': 'This field cannot be updated.'})
        elif 'username' not in attrs:
            raise serializers.ValidationError({'username': 'This field is required.'})

        return attrs
