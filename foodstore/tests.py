from django.test import TestCase, Client
from foodstore import models
from django.urls import reverse
from django.contrib.auth.models import User


class ProductReviewTestCase(TestCase):
    def setUp(self):
        # Create a category, a product, 2 user
        self.category = models.Category.objects.create(name="Category A")
        self.user_a = User.objects.create_user(
            username="usera", password="12345678")
        self.user_b = User.objects.create_user(
            username="userb", password="12345678")


    def test_add_first_review_to_product(self):
        product = models.Product.objects.create(
            name="Product A", price="20", status=0,
            ship="", category=self.category)
        c = Client()
        c.login(username="usera", password="12345678")
        c.post(reverse('review-create', kwargs={
            'category': self.category.slug,
            'product_id': product.pk
        }), data={
            'rate': 4,
            'comment': "Test"
        })
        self.assertEqual(
            models.Product.objects.get(
                pk=product.pk).rating, float(4))


    def test_an_user_can_only_review_each_product_once(self):
        product = models.Product.objects.create(
            name="Product A", price="20", status=0,
            ship="", category=self.category)
        c = Client()
        c.login(username="usera", password="12345678")
        c.post(reverse('review-create', kwargs={
            'category': self.category.slug,
            'product_id': product.pk,
        }), data={
            'rate': 4,
            'comment': "Test"
        })
        result = c.post(reverse('review-create', kwargs={
            'category': self.category.slug,
            'product_id': product.pk,
        }), data={
            'rate': 3,
            'comment': "Another Test"
        })
        self.assertEqual(result.status_code, 400)

    
    def test_many_users_review_interaction_on_product_rating(self):
        """
        Product rating = average of all rating, even when the rating is changed or delete
        """
        product = models.Product.objects.create(
            name="Product A", price="20", status=0,
            ship="", category=self.category)
        c = Client()

        # User A add a review
        c.login(username="usera", password="12345678")
        c.post(reverse('review-create', kwargs={
            'category': self.category.slug,
            'product_id': product.pk,
        }), data={
            'rate': 4,
            'comment': "Test"
        })
        c.logout()

        # User B add another review
        c.login(username="userb", password="12345678")
        c.post(reverse('review-create', kwargs={
            'category': self.category.slug,
            'product_id': product.pk,
        }), data={
            'rate': 3,
            'comment': "Another Test"
        })
        self.assertEqual(models.Product.objects.get(
            pk=product.pk).rating, 3.5)

        # User B edit that review
        review = product.review_set.get(user=self.user_b)
        c.post(reverse('review-update', kwargs={
            'category': self.category.slug,
            'product_id': product.pk,
            'review_id': review.pk
        }), data={
            'rate': 2,
            'comment': 'Test comment'
        })
        self.assertEqual(models.Product.objects.get(
            pk=product.pk).rating, 3)
            
        # User B delete review
        c.post(reverse('review-delete', kwargs={
            'category': self.category.slug,
            'product_id': product.pk,
            'review_id': review.pk
        }))
        self.assertEqual(models.Product.objects.get(
            pk=product.pk).rating, 4)



class ProductTestCase(TestCase):
    def setUp(self):
        cat_a = models.Category.objects.create(
            name="CategoryA")
        cat_b = models.Category.objects.create(
            name="CategoryB")
        # Create products for cat_a
        models.Product.objects.create(
            name="Prod abcd", price="20", status=0,
            ship="", category=cat_a)
        models.Product.objects.create(
            name="Prod bcde", price="20", status=0,
            ship="", category=cat_a)
        # Create product for cat_b
        models.Product.objects.create(
            name="Prod cdef", price="20", status=0,
            ship="", category=cat_b)
        models.Product.objects.create(
            name="Prod defg", price="20", status=0,
            ship="", category=cat_b)
    

    def test_query_products_by_name(self):
        c = Client()
        response = c.get(reverse('products'), data={
            'q': 'cde'
        })
        self.assertContains(response, "Prod bcde")
        self.assertContains(response, "Prod cdef")


    def test_add_favorite_product_store_data_in_session(self):
        c = Client()
        category = models.Category.objects.all()[0]
        products = models.Product.objects.filter(
            category=category)
        list_objs = []
        for product in products:
            c.get(reverse('product-set-favorite', kwargs={
                'category': category,
                'product_id': product.pk
            }), data={
                'next': ''
            })
            list_objs.append(product.pk)
        try:
            favorite_product_data = c.session["favorite_products"]
        except KeyError:
            favorite_product_data = None
        self.assertIsNotNone(favorite_product_data)
        self.assertEqual(
            favorite_product_data['length'], 2)
        self.assertEqual(
            favorite_product_data['object_ids'], list_objs)


    def test_list_favorite_product(self):
        """
        Firstly, choose 2 products as favorite. The views need to contain names of the 2 products
        """
        c = Client()
        category = models.Category.objects.all()[0]
        products = models.Product.objects.filter(
            category=category)
        list_product_names = []
        for product in products:
            c.get(reverse('product-set-favorite', kwargs={
                'category': category,
                'product_id': product.pk
            }), data={
                'next': ''
            })
            list_product_names.append(product.name)
        response = c.get(reverse('product-list-favorite'))
        for name in list_product_names:
            self.assertContains(response, name)