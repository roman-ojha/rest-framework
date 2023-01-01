from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Student


# Creating class extends from 'HyperlinkedModelSerializer'
class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'roll', 'city']
        # here by default it provide 'url' field as well
        # URL provide the detail for that particular record
        # EX: for roll: 1, url: "http://127.0.0.1:8000/studentapi/1/"
