from rest_framework.serializers import ModelSerializer
from core.models import Group


class GroupSerializer(ModelSerializer):
    """serializer for group object"""

    class Meta:
        model = Group
        fields = [
            "GroupId",
            "GroupName",
        ]