from rest_framework import serializers
from .models import AlbumReview, AlbumReviewComment, AlbumReviewLike


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    review = serializers.ReadOnlyField(source='album_review_id.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'user_id', 'review', 'review_content']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comment_count = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True, read_only=True)

    def get_comment_count(self, obj):
        return AlbumReviewComment.objects.filter(album_review_id=obj).count()

    class Meta:
        model = AlbumReview
        fields = ['user', 'user_id', 'album_id', 'content', 'score', 'comment_count', 'comments']


class AlbumReviewLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumReviewLike
        fields = ['id']
