from django.test import TestCase
from .models import Product, ProductType, Review

class ProductTypeTest(TestCase):
   def test_string(self):
       type=ProductType(typename="Tablet")
       self.assertEqual(str(type), type.typename)

def test_table(self):
     self.assertEqual(str(productType._meta.db_table), 'producttype')

class ProductTest(TestCase):
   #set up one time sample data
   def setup(self):
       type = ProductType(typename='laptop')
       product=Product(productname='Lenovo', producttype=type, productprice='500.00')
       return product
   def test_string(self):
       prod = self.setup()
       self.assertEqual(str(prod), prod.productname)
  
   #test the discount property
   def test_discount(self):
       prod=self.setup()
       self.assertEqual(prod.memberdiscount(), 25.00)

   def test_type(self):
       prod=self.setup()
       self.assertEqual(str(prod.producttype), 'laptop')

   def test_table(self):
       self.assertEqual(str(Product._meta.db_table), 'product')



class ReviewTest(TestCase):
   def test_string(self):
       rev=Review(reviewtitle="Best Review")
       self.assertEqual(str(rev), rev.reviewtitle)

   def test_table(self):
       self.assertEqual(str(Review._meta.db_table), 'review')
