from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewLike


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'band_id']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = AlbumReview
        fields = ['user', 'album_id', 'content', 'score']
