from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from .models import ProductType, Product, Review

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'pythonclubapp/types.htm' ,{'type_list' : type_list})
# Create your views here.
def index (request):
    return render(request, 'pythonclubapp/index.htm')

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'pythonclubapp/products.htm', {'products_list': products_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    discount=prod.memberdiscount
    reviews=Review.objects.filter(product=id).count()
    context={
        'prod' : prod,
        'discount' : discount,
        'reviews' : reviews,
    }
    return render(request, 'pythonclubapp/proddetails.htm', context=context)
