from rest_framework import viewsets
from api.models import Post
from api.serializers import PostSerializer, PostUpdateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return PostUpdateSerializer
        return PostSerializer
