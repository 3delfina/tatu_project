import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tatu_project.settings')

import django
django.setup()
from tatu.models import Page, UserProfile, Picture, Comment

def populate():
    user_profiles = [
        {"fullname": "Jeremy Smith",
         "username": "jez97",
         "picture": ???,
         "workplace": "Glasgow Uni",
         "phone_no": "07777777777",
         "website": "rossisthebest.com",
         "email": "rosscee1998@gmail.com"},
        {"fullname": "John Smith",
         "username": "john_smith_78",
         "picture": ???,
         "workplace": "Microsoft",
         "phone_no": 07777777778,
         "website": "johnisthebest.com",
         "email": "johnsmith3@gmail.com"},
    ]

    comments = [
        {"text": "this tattoo sucks. die",
         "date": datetime.datetime(2018,03,16)},
        {"text": "This work is amazing! You should be proud!",
         "date": datetime.datetime(2018,03,12)}
        {"text": "uhmm. it's interesting",
         "date": datetime.datetime(2018,03,15)}
    ]

    pictures = [
        {"tattoo_picture": ???,
         "tag": "watercolour",
         "rating": 7},
        {"tattoo_picture": ???,
         "tag": "tribal",
         "rating": 5},
        {"tattoo_picture": ???,
         "tag": "dotwork",
         "rating": 8}
    ]

def add_comment(text, date=datetime.date.now()):
    c = Comment.objects.get_or_create(text=text, date=date)
    c.save()
    return c

def add_picture():
    p = Picture.objects.get_or_create()
    p.save()
    return p

def add_user_profile():
    u = UserProfile.objects.get_or_create()
    u.save()
    return u

if __name__ == '__main__':
    print("Starting Tatu population script...")
    populate()
