from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_creates_user_and_logs_in(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'role': 'buyer',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        }
        resp = self.client.post(reverse('register'), data)
        # registration view should redirect on success
        self.assertIn(resp.status_code, (301, 302))

        # user should exist in DB and be active
        user = User.objects.filter(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.role, 'buyer')
        self.assertTrue(user.is_active)

        # client should be authenticated (follow redirect and check request.user)
        follow = self.client.get(resp.url)
        self.assertTrue(follow.wsgi_request.user.is_authenticated)

    def test_register_page_renders(self):
        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)

    def test_login_with_credentials(self):
        # create user
        user = User.objects.create_user(username='loginuser', email='login@example.com', password='pass12345')
        data = {'username': 'loginuser', 'password': 'pass12345'}
        resp = self.client.post(reverse('login'), data)
        self.assertIn(resp.status_code, (301, 302))
        follow = self.client.get(resp.url)
        self.assertTrue(follow.wsgi_request.user.is_authenticated)
