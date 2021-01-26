from rest_framework.serializers import ModelSerializer
from core.models import Leader


class LeaderSerializer(ModelSerializer):
    """serializer for leader object"""

    class Meta:
        model = Leader
        fields = [
            "LeaderId",
            "Student",
            "Group",
            "Position",
        ]