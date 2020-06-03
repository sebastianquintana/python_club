from django import forms
from .models import Product, ProductType, Review
from .forms import ProductForm

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'pythonclubapp/newproduct.htm', {'form': form})

