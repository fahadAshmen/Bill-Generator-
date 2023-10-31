from rest_framework import serializers


class BillItemSerializer(serializers.Serializer):    
    item_name = serializers.CharField(max_length=155)
    quantity = serializers.IntegerField()
    rate = serializers.DecimalField(max_digits=10, decimal_places=2)