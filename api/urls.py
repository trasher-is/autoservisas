from django.urls import path, include
from .views import AlbumReviewList, AlbumReviewDetail, AlbumReviewCommentList, AlbumReviewCommentDetail


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('review', AlbumReviewList.as_view()),
    path('reviews/<int:pk>', AlbumReviewDetail.as_view()),
    path('reviews/<int:pk>/comments', AlbumReviewCommentList.as_view()),
    path('comments/<int:pk>', AlbumReviewCommentDetail.as_view())

]
