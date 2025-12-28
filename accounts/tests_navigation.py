from django.test import TestCase, Client
from django.urls import reverse

class NavigationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_register_links_present_on_homepage(self):
        resp = self.client.get(reverse('homepage'))
        self.assertContains(resp, reverse('login'))
        self.assertContains(resp, reverse('register'))

    def test_login_page_available(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_logout_redirects_home(self):
        # GET logout should redirect to homepage (configured in urls.py)
        resp = self.client.get(reverse('logout'))
        # logout redirects (302) to homepage
        self.assertIn(resp.status_code, (302, 301))
        # follow the redirect
        follow = self.client.get(resp.url)
        self.assertEqual(follow.status_code, 200)
