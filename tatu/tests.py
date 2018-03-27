import os
from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles import finders

from django.contrib.auth.models import User
from tatu.models import UserProfile, Post, Comment
from django.core.files.uploadedfile import SimpleUploadedFile

class StaticFileTests(TestCase):
    # the return value of finders.find(<filepath>) is not NONE if static file loads correctly
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
        self.assertTemplateUsed(response, 'tatu/Browse_base.html')


class ModelTests(TestCase):

    def setUp(self):
        MEDIA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')

        u1 = User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
        u2 = User.objects.create_user('Ringo', 'starr@thebeatles.com', 'ringopassword')

        p1 = UserProfile.objects.create(user=u1, website='lennon.com')
        p2 = UserProfile.objects.create(user=u2, website='starr.com')

        image = SimpleUploadedFile(name='test_image.jpg',
                                   content=open(os.path.join(MEDIA_DIR, 'test', 'test_image.jpg'), 'rb').read(),
                                   content_type='image/jpeg')

        post = Post.objects.create(category='TR',
                                   author=u1,
                                   image=image,
                                   description='My best work to date')

        Comment.objects.create(thread=post, poster=p2, text='Incredible!')

    def test_profile_user_relationship(self):
        # ensure Ringo's user instance is associated with his UserProfile instance
        try:
            ringo_profile = UserProfile.objects.get(website='starr.com')
            User.objects.get(userprofile=ringo_profile)
        except:
            self.fail("Profile creation is dysfunctional.")

    def test_post_creation_successful(self):
        # ensure John's post was created by checking its existence
        try:
            Post.objects.get(author=User.objects.get(username='John'))
        except Post.DoesNotExist:
            self.fail('Post creation is dysfunctional.')

    def test_comment_creation_successful(self):
        # ensure Ringo's comment on John's post was created by checking its existence
        try:
            ringo = User.objects.get(username='Ringo')
            profile = UserProfile.objects.get(user=ringo)
            post = Post.objects.get(author=User.objects.get(username='John'))
            Comment.objects.get(thread=post, poster=profile)
        except:
            self.fail("Comment creation is dysfunctional.")

