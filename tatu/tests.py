from django.test import TestCase

class IndexPageTests(TestCase):
    def test_index_page_loads_okay(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

class TattoosPageTests(TestCase):

class CreateAccountPageTests(TestCase):

class LoginPageTests(TestCase):

class ProfilePageTests(TestCase):

class RateArtistPageTests(TestCase):

class ModelTests(TestCase):
    
    def setUp(self):
        try:
            from population_script import populate
            populate()
        except ImportError:
            print("The module 'population_script' does not exist")
        except NameError:
            print("The function 'populate()' does not exist, or is not correct")
        except:
            print("Something weird went wrong in the populate() function")

    def get_page(self, name):
        from tatu.models import Page
        try:
            url = Page.objects.get(url=url)
        except Page.DoesNotExist:
            url = None
        return url

    # once population script, create tests here checking pages have been added
    # like shown below (just change page urls)
    def test_(((page url)))_added(self):
        page = self.get_page("page url")
        self.assertIsNotNone(page)

    def test_comment_date_not_in_future(self):
        """
        the associated date of comments should never be in the future
        """
        current_date = date.today()
        #future_comment = Comment(date=date)
        self.assertEqual(comment_date < current_date)

    def test_comment_cannot_exceed_length_200(self):
        text = "a" * 201
        comment = Comment(text=date)

class ViewTests(TestCase):
    

class TatuTests(TestCase):
    def test_
    
    def test_1(self):
        pass

    def test_2(self):
        pass
