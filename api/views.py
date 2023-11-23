from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Band, Album, Song, AlbumReview, AlbumReviewLike
from .serializers import AlbumSerializer, AlbumReviewSerializer


class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
