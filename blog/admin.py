from django.contrib import admin
from .models import StreamPlatform, WatchList, Review

@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'website')

@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('title', 'storyline', 'platform', 'active', 'avg_rating', 'number_rating', 'created')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_user', 'rating', 'description', 'watchlist', 'active', 'created', 'update')
