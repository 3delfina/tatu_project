from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles import finders

class StaticFileTests(TestCase):
    # the return value of finders.find(<filename>) is not NONE if static file loads correctly
    def test_serving_home_background(self):
        self.assertIsNotNone(finders.find('css/home.png'))

    def test_serving_browse_background(self):
        self.assertIsNotNone(finders.find('css/browse.png'))

    def test_serving_login_background(self):
        self.assertIsNotNone(finders.find('css/login.png'))

    def test_serving_register_background(self):
        self.assertIsNotNone(finders.find('css/register.png'))

    def test_serving_clear_background(self):
        self.assertIsNotNone(finders.find('css/clear_white.png'))

    def test_serving_other_background(self):
        self.assertIsNotNone(finders.find('css/other.png'))

class IndexPageTests(TestCase):

    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'tatu/index.html')

class RegisterPageTests(TestCase):

    def test_register_using_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'tatu/register.html')


class LoginPageTests(TestCase):

    def test_login_using_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'tatu/login.html')


class ContactPageTests(TestCase):

    def test_contact_using_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'tatu/contact.html')


class FAQPageTests(TestCase):

    def test_faq_using_template(self):
        response = self.client.get(reverse('faq'))
        self.assertTemplateUsed(response, 'tatu/faq.html')


class ArtistsPageTests(TestCase):

    def test_artists_using_template(self):
        response = self.client.get(reverse('artists'))
        self.assertTemplateUsed(response, 'tatu/artists.html')


"""
class ProfilePageTests(TestCase):

    def test_profile_using_template(self):
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'tatu/profile.html')
"""

class TattoosPageTests(TestCase):

    def test_profile_using_template(self):
        response = self.client.get(reverse('tattoos'))
        self.assertTemplateUsed(response, 'tatu/tattoos.html')
