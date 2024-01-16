# serializers.py
from rest_framework import serializers
from datetime import datetime

from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image_url']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'discount_percentage',
                  'rating', 'stock', 'brand', 'category', 'thumbnail',
                  'created_at', 'updated_at', 'images']

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        product = Product.objects.create(**validated_data)
        for image_data in images_data.values():
            ProductImage.objects.create(product=product, image_url=image_data)
        return product
# class Product(serializers.Serializer):
#     id = serializers.IntegerField()
#     title =serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     discount_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
#     rating = serializers.FloatField()
#     stock = serializers.IntegerField()
#     brand = serializers.CharField(max_length=255)
#     category = serializers.CharField(max_length=255)
#     thumbnail = serializers.URLField()
#     created_at = serializers.DateTimeField(auto_now_add=True)
#     updated_at = serializers.DateTimeField(auto_now=True)
#     created_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         validated_data['created_at'] = datetime.now()
#         return super(Product, self).create(validated_data)
    


# class ProductImage(serializers.Serializer):
#     product = serializers.ForeignKey(Product, related_name='images', on_delete=serializers.CASCADE)
#     image_url = serializers.URLField()