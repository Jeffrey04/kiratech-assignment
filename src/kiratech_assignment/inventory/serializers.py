from rest_framework import serializers


class InventorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    supplier = serializers.CharField(source="supplier.name")
    availability = serializers.BooleanField(required=False)
