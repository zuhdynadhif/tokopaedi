from django.test import TestCase, Client

# Create your tests here.

# import Product pada models.py
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main/main.html')
    
    def test_attribute_field_type(self):
        product = Product(
            name = 'Kursi Gaming',
            price = 2000000,
            amount = 1,
            description = 'Kursi Gaming tidak gratis ya'
        )
        self.assertEqual(type(product.name), str)
        self.assertEqual(type(product.price), int)
        self.assertEqual(type(product.amount), int)
        self.assertEqual(type(product.description), str)
    
    def test_attribute_field_value(self):
        product = Product(
            name = 'Kursi Gaming',
            price = 2000000,
            amount = 1,
            description = 'Kursi Gaming tidak gratis ya'
        )
        self.assertEqual(product.name, 'Kursi Gaming')
        self.assertEqual(product.price, 2000000)
        self.assertEqual(product.amount, 1)
        self.assertEqual(product.description, 'Kursi Gaming tidak gratis ya')