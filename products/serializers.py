from rest_framework import serializers
from .models import Product

#to return objects in the API for products
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# no serializer for 'User' model as we will just return random IDs there