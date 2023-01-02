from .models import Song, Singer
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    # Using 'SongSerializer' and adding field to get the song sang by the singer
    # Nested Serializer
    song = SongSerializer(many=True, read_only=True)
    # NOTE: 'song' is the related_name specify inside 'Song' model 'singer' field

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
