from .views import *
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


# router=DefaultRouter()
router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet,basename='products')
product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls))
]
