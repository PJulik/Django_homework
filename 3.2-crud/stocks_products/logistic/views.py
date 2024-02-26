from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title']
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    filterset_fields = ['id', 'products']
    ordering_fields = ['id', 'address']
    search_fields = ['products__title']
    # при необходимости добавьте параметры фильтрации
