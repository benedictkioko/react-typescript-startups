from rest_framework.serializers import ModelSerializer
from core.models import Subject


class SubjectSerializer(ModelSerializer):
    """serializer for subject object"""

    class Meta:
        model = Subject
        fields = [
            "SubjectId",
            "SubjectName",
            "Abbreviation",
        ]
