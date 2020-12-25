from django.test import TestCase, Client
from django.urls import reverse

GUEST_USER_DATA = {
    'first_name': 'A',
    'last_name': 'B',
    'email': 'email1@mail.com',
    'username': 'testuser1',
    'password': '12345678'
}

STAFF_USER_DATA = {
    'first_name': 'C',
    'last_name': 'D',
    'email': 'email2@mail.com',
    'username': 'testuser2',
    'password': '12345678',
    'is_staff': True
}


# Create your tests here.
class AdminPermissionTestCase(TestCase):
    def setUp(self):
        """
        Register 2 user, 1 admin and 1 guest
        """
        c = Client()
        response_guest = c.post(reverse('register'), GUEST_USER_DATA)
        self.assertEqual(response_guest.status_code, 200)
        response_staff = c.post(reverse('register'), STAFF_USER_DATA)
        self.assertEqual(response_staff.status_code, 200)