
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, filters
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .models import *
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        print(self.kwargs)
        return {'slug': self.kwargs['product_slug']}

    def get_queryset(self):
        product = get_object_or_404(Product, slug=self.kwargs['product_slug'])
        return Review.objects.filter(product=product)
