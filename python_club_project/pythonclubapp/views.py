from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from .models import ProductType, Product, Review

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'pythonclubapp/types.htm' ,{'type_list' : type_list})
# Create your views here.
def index (request):
    return render(request, 'pythonclubapp/index.htm')
