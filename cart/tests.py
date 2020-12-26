from django.test import TestCase, Client
from django.urls import reverse

from foodstore import models as foodstore_models



class CartTestCase(TestCase):
    def setUp(self):
        self.cat_a = foodstore_models.Category.objects.create(
            name="CategoryA")
        # Create products for cat_a
        self.product_a = foodstore_models.Product.objects.create(
            name="Prod abcd", price="20", status=0,
            ship="", category=self.cat_a)
        self.product_b = foodstore_models.Product.objects.create(
            name="Prod bcde", price="20", status=0,
            ship="", category=self.cat_a)


    def test_add_product_to_cart_update_session_data(self):
        c = Client()
        c.post(reverse('product-add-to-cart', kwargs={
            'category': self.cat_a.slug,
            'product_id': self.product_a.pk
        }), data={
            'quantity': 3
        })
        try:
            cart_session_data = c.session['cart']
        except KeyError:
            cart_session_data = None
        self.assertIsNotNone(cart_session_data)
        self.assertEqual(cart_session_data['length'], 1)
        self.assertEqual(cart_session_data['total_price'], 60)
        try: 
            product_a_cart_data = cart_session_data['cart_data'][str(
                self.product_a.pk)]
        except KeyError:
            product_a_cart_data = None
        self.assertEqual(product_a_cart_data, {
            'amount': 3,
            'price': float(20),
            'total_price': float(60)
        })


    def test_add_same_product_twice(self):
        c = Client()
        c.post(reverse('product-add-to-cart', kwargs={
            'category': self.cat_a.slug,
            'product_id': self.product_a.pk
        }), data={
            'quantity': 3
        })
        c.post(reverse('product-add-to-cart', kwargs={
            'category': self.cat_a.slug,
            'product_id': self.product_a.pk
        }), data={
            'quantity': 3
        })
        self.assertEqual(c.session['cart']['length'], 1)