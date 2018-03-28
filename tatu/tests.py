import os
from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles import finders

from tatu.models import *
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.test import Client


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


class TemplateTests(TestCase):

    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'tatu/index.html')

    def test_register_using_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'tatu/register.html')

    def test_login_using_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'tatu/login.html')

    def test_contact_using_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'tatu/contact.html')

    def test_faq_using_template(self):
        response = self.client.get(reverse('faq'))
        self.assertTemplateUsed(response, 'tatu/faq.html')

    def test_artists_using_template(self):
        response = self.client.get(reverse('artists'))
        self.assertTemplateUsed(response, 'tatu/artists.html')


class TattoosPageTests(TestCase):

    def test_profile_using_template(self):
        response = self.client.get(reverse('tattoos'))
        self.assertTemplateUsed(response, 'tatu/Browse_base.html')


class ModelTests(TestCase):

    def setUp(self):

        MEDIA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')

        u1 = User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
        u2 = User.objects.create_user('Ringo', 'starr@thebeatles.com', 'ringopassword')

        p1 = UserProfile.objects.create(user=u1, website='http://www.lennon.com/')
        p2 = UserProfile.objects.create(user=u2, website='http://www.starr.com/')

        image = SimpleUploadedFile(name='test_image.jpg',
                                   content=open(os.path.join(MEDIA_DIR, 'test', 'test_image.jpg'), 'rb').read(),
                                   content_type='image/jpeg')

        post = Post.objects.create(category='TR',
                                   author=u1,
                                   image=image,
                                   description='My best work to date')

        Comment.objects.create(thread=post, poster=p2, text='Incredible!')

        Like.objects.create(user=u2, post=post)

    def test_profile_user_relationship(self):
        # ensure Ringo's user instance is associated with his UserProfile instance
        try:
            ringo_profile = UserProfile.objects.get(website='http://www.starr.com/')
            User.objects.get(userprofile=ringo_profile)
        except:
            self.fail('Profile creation is dysfunctional.')

    def test_post_creation_successful(self):
        # ensure John's post was created by checking its existence
        try:
            Post.objects.get(author=User.objects.get(username='John'))
        except Post.DoesNotExist:
            self.fail('Post has not been properly created')
        except:
            self.fail('Something a bit weird went wrong in post creation')

    def test_comment_creation_successful(self):
        # ensure Ringo's comment on John's post was created by checking its existence
        try:
            ringo = User.objects.get(username='Ringo')
            profile = UserProfile.objects.get(user=ringo)
            post = Post.objects.get(author=User.objects.get(username='John'))
            Comment.objects.get(thread=post, poster=profile)
        except Comment.DoesNotExist:
            self.fail('Comment has not been properly created')
        except:
            self.fail('Something a bit weird went wrong in comment creation')

    def test_like_creation_successful(self):
        # ensure Ringo liking John's post was successful by checking for its existence
        try:
            ringo = User.objects.get(username='Ringo')
            post = Post.objects.get(author=User.objects.get(username='John'))
            Like.objects.get(user=ringo, post=post)
        except Like.DoesNotExist:
            self.fail('Like has not been properly created')
        except:
            self.fail('Something a bit weird went wrong in like creation')

    def test_profile_workplace_max_length(self):
        try:
            ringo = User.objects.get(username='Ringo')
            profile = UserProfile(
                user=ringo,
                website='http://www.starr.com/',
                workplace='a'*101
            )
            profile.full_clean()
            print(profile)
            self.fail('Character limit on workplace attribute within profile not enforced')
        except:
            pass


class FormTests(TestCase):

    def setUp(self):
        try:
            from forms import CommentForm
            from forms import PostForm
        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('One of the form classes are non-existent or incorrect')
        except:
            print('Something freaky went wrong yee-ha')


class OtherTests(TestCase):

    def test_login_works(self):
        # creates user, then attempts to log in using those credentials
        user = User.objects.create_user(username='test_user')
        user.set_password('thisismypassword')
        user.save()

        c = Client()
        logged_in = c.login(username='test_user', password='thisismypassword')
        self.assertTrue(logged_in)

