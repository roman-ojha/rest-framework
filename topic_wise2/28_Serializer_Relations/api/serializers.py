from .models import Song, Singer
from rest_framework import serializers


# Serializing both the model and creating relation with it
class SongSerializer(serializers.ModelSerializer):
    # if you want to see the value returned from Singer Model '__str__' function on 'singer' field in that case you have to specify the 'StringRelatedField'
    singer = serializers.StringRelatedField(read_only=True)
    # EX:
    """
        {
        "id": 1,
        "title": "Tum hi ho",
        "singer": "Ariit",
        "duration": 4
    }
    """

    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    # if you want to get the Songs sing by the singer from this serializer in that case we have to add song here
    # NOTE: we have to specify the field that we specify on 'Singer' model 'related_name'
    song = serializers.StringRelatedField(many=True, read_only=True)
    # StringRelatedField: return '__str__' function value
    # EX:
    """
        {
        "id": 1,
        "name": "Ariit",
        "gender": "male",
        "song": [
            "Tum hi ho" // return value which is being returned by '__str__' function in Model
        ]
    }, 
    """

    # If you will not specify the 'song' field with 'StringRelatedField' then you will get
    # EX:
    """
        "id": 1,
        "name": "Ariit",
        "gender": "male",
        "song": [
            1
        ]
    """

    song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # PrimaryKeyRelatedFiled: return 1, 2 (primary key)

    song = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='song-detail')
    # EX:
    """
        "id": 1,
        "name": "Ariit",
        "gender": "male",
        "song": [
            "http://127.0.0.1:8000/song/1/"
        ] 
    """

    song = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='title')
    # EX:
    """
        "id": 1,
        "name": "Ariit",
        "gender": "male",
        "song": [
            "Tum hi ho" // title
        ]
    """

    #
    song = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='duration')
    # EX:
    """
        "id": 1,
        "name": "Ariit",
        "gender": "male",
        "song": [
            4 // duration
        ]
    """

    song = serializers.HyperlinkedIdentityField(
        many=True, read_only=True, view_name='song-detail')
    # EX:
    """
        "id": 1,
        "name": "Ariit",
        "gender": "male",
        "song": [
            "http://127.0.0.1:8000/song/1/"
        ]
    """

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
