from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from mysite1.models import SalesOrger
from mysite1.serializers import OrderSerializer


# Create your views here.
def index_page(request):
    return render(request, 'index.html', {'orders': SalesOrger.objects.all()})

class OrderView(ModelViewSet):
    queryset = SalesOrger.objects.all()
    serializer_class = OrderSerializer