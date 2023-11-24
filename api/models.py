from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=500)
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=500)
    duration = models.IntegerField()
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    score = models.IntegerField()

    def __str__(self):
        return f'by {self.user}, score: {self.score}, body: {self.content}'


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name='comments')
    review_content = models.CharField(max_length=2000)

    def __str__(self):
        return f'by {self.user}: {self.review_content}'


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
