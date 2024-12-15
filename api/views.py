from django.shortcuts import render
from rest_framework import viewsets
from api.models import Post
from api.serializers import PostSerializer
from api.services import post_service

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer