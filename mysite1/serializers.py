from rest_framework.serializers import ModelSerializer

from mysite1.models import SalesOrger


class OrderSerializer(ModelSerializer):
    class Meta:
        model = SalesOrger
        fields = ['amount', 'description']