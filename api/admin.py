from django.contrib import admin

from .models import Band, Album, Song, AlbumReview, AlbumReviewLike


class BandAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'band_id')


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'album_id')


class AlbumReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'album_id', 'content', 'score')


class AlbumReviewLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'album_review_id')


admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(AlbumReview, AlbumReviewAdmin)
admin.site.register(AlbumReviewLike, AlbumReviewLikeAdmin)
