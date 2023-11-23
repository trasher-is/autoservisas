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
    duration = models.IntegerField(null=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    score = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user} - {self.album_id} - {self.score}'


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
