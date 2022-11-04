from django.shortcuts import render

from mysite1.models import SalesOrger


# Create your views here.
def index_page(request):
    return render(request, 'index.html', {'orders': SalesOrger.objects.all()})
