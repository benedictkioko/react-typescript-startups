from rest_framework.serializers import ModelSerializer
from core.models import Score


class ScoreSerializer(ModelSerializer):
    """serializer for scores object"""

    class Meta:
        model = Score
        fields = [
            "ScoreId",
            "Student",
            "Subject",
            "Term",
            "score",
        ]