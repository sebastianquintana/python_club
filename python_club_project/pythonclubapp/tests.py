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


class New_Product_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=ProductType.objects.create(typename='laptop')
        self.prod = Product.objects.create(productname='product1', producttype=self.type, user=self.test_user, productprice=500, productentrydate='2019-04-02',producturl= 'http://www.dell.com', productdescription="a product")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newproduct'))
        self.assertRedirects(response, '/accounts/login/?next=/pythonclubapp/newProduct/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newproduct'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pythonclubapp/newproduct.htm')
