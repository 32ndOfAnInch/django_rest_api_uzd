from rest_framework import serializers
from . import models

class SongSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='band.name')

    class Meta:
        model = models.Song
        fields = ['id', 'name', 'duration', 'band']

    
class SongReviewSerializer(serializers.ModelSerializer):
    song = serializers.ReadOnlyField(source='song.name')

    class Meta:
        model = models.SongReview
        fields = ['id', 'user', 'song', 'content', 'score']