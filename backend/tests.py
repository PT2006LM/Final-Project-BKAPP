from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

GUEST_USER_DATA = {
    'username': 'testuser1',
    'password': '12345678',
}

STAFF_USER_DATA = {
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
        User.objects.create_user(**GUEST_USER_DATA)
        User.objects.create_user(**STAFF_USER_DATA)


    def test_anonymous_user_cant_access_admin(self):
        c = Client()
        # Guest
        response = c.get(reverse('index'))
        # Being redirected due to not being a staff
        self.assertEqual(response.status_code, 302)


    def test_guest_user_cant_access_admin(self):
        c = Client()
        # Login as guest user
        result = c.login(username=GUEST_USER_DATA['username'],
            password=GUEST_USER_DATA['password'])
        self.assertTrue(result)
        response = c.get(reverse('index'))
        # Being redirected due to not being a staff
        self.assertEqual(response.status_code, 302)


    def test_staff_can_access_admin(self):
        """
        Views with staff_member_require can only accessed with staff user
        """
        c = Client()
        # Login as staff
        result = c.login(username=STAFF_USER_DATA['username'],
            password=STAFF_USER_DATA['password'])
        self.assertTrue(result)
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)