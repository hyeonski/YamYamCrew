# api/views.py
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
