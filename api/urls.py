from django.urls import path, include
from .views import AlbumList, AlbumReviewList

urlpatterns = [
    path('albums', AlbumList.as_view()),
    path('albums-review', AlbumReviewList.as_view()),
]
