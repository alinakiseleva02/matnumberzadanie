from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Manufacturer, Product
from .serializer import ManufacturerSerializer, ProductSerializer
from django.utils.decorators import method_decorator

class ManufacturerViewsets(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    
    @action(methods=['GET'], detail=False, url_path='russian')
    def russian_manufacturers_list(self, request):
        queryset = self.get_queryset().filter(country='Россия')
        serializer = self.get_serializer(queryset, many-True)
        return Response(serializer.data)
    
def perform_create(self, serializer):
    name = serializer.data['name']
    if not name.startwith('000'):
        name = '000' + name
        serializer.validated_data['name'] = name
    return super().perform_create(serializer)
    
class ProductViewsets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer