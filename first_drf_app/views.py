from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Number
from .serializer import NumberSerializer
import random

class NumberViewSets(ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

    @action(methods=['GET'], detail=False, url_path='random')
    def get_random_number(self, request):
        min_val = int(request.GET.get('min', 0))
        max_val = int(request.GET.get('max', 100))
        
        random_number = random.randint(min_val, max_val)
        
        return Response({"random_number": random_number})