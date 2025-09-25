from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # للقراءة فقط
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',  # يربط الـ ID بالـ ForeignKey
        write_only=True
    )
    class Meta:
        model=Product
        fields=['category','category_id','id','title','description','price','slug']


class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model=Review
        fields='__all__'
    def create(self, validated_data):
        product_slug=self.context['slug']  
        product= Product.objects.get(slug=product_slug)
        validated_data['product']=product 
        return super().create(validated_data)

    