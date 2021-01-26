from rest_framework.serializers import ModelSerializer
from core.models import Term


class TermSerializer(ModelSerializer):
    """serializer for term object"""

    class Meta:
        model = Term
        fields = [
            "TermId",
            "TermName",
        ]