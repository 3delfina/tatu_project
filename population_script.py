import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tatu_project.settings')

import django
django.setup()
from tatu.models import UserProfile, Post, Comment
from django.contrib.auth.models import User

# UserProfile (avatar, workplace, website, phone_number)          [DONE]
# Post (category, author, image, description, date, favourites)
# Comment (text, date)

# instance: if the user's id is 13, their avatar will be saved to:
# .../tatu_project/media/user_13/avatar/(filename)

"""
def user_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # change this to the path pages are saved at
    return 'user_{0}/avatar/{1}'.format(instance.user.id, filename)
"""

def populate():

    users = [
        {"username": "jezza32",
         "first_name": "John",
         "last_name": "Smith",
         "password": "password",
         "email": "jezza32@gmail.com"},
        {"username": "xo_g1ve_m3_h0p3_xo",
         "first_name": "Hannah",
         "last_name": "Spritz",
         "password": "teletubbies32",
         "email": "hannah.spritz@gmail.com"},
        {"username": "pizzaboy82",
         "first_name": "Stephen",
         "last_name": "O'Connelly",
         "password": "pizzaisthebest",
         "email": "pizzaboy82@gmail.com"},
        ]

# mapping users to user_profiles just by index within their lists
# probably not the best way, but it should work?? is there a better way?

    user_profiles = [
        {"avatar": "Users/rossclark/workspace/pop/a",
         "workplace": "Tattoo Heaven",
         "website": "www.tattooheaven.com",
         "phone_number": 07783745929},
        {"avatar": "Users/rossclark/workspace/pop/b",
         "workplace": "Lucky Cat Tattoo",
         # website missing - i think it can be blank? let's test that
         "phone_number": 07792825577},
        {"avatar": "Users/rossclark/workspace/pop/c",
         "workplace": "Otzi Tattoos",
         "website": "www.tattooheaven.com",
         "phone_number": 07783745929}
        ]

# posts are also associated with users
    posts = [
        {"category": "RL",
         "image": "Users/rossclark/workspace/pop/a",
         "description": "Perhaps the best tattoo I've ever completed! Ultra realistic.",
         "date": datetime.datetime(2018,03,16),
         "favourites": 5},
        {"category": "GM",
         "image": "Users/rossclark/workspace/pop/b",
         "description": "aaa",
         "date": datetime.datetime(2018, 03, 12),
         "favourites": 13},
        {"category": "BW",
         "image": "Users/rossclark/workspace/pop/c",
         "description": "aaa",
         "date": datetime.datetime(2018, 03, 15),
         "favourites": 2}
    ]

# comments are also associated with individual posts & individual users
    comments = [
        {"text": "this tattoo sucks. die",
         "date": datetime.datetime(2018,03,20)},
        {"text": "This work is amazing! You should be proud!",
         "date": datetime.datetime(2018,03,19)},
        {"text": "uhm. it's interesting",
         "date": datetime.datetime(2018,03,17)}
    ]

    for ix, entry in enumerate(users):
        add_user(entry)
        add_user_profile(user_profiles[ix])
        # do we need to pass the User instance on in order to create the UserProfile instance?
        # in that case, you'd want to set add_user(entry) = user, then pass user into
        # add_user_profile, and within that, pass user=user into the get_or_create function

def add_user(entry):
    username = entry["username"]
    first = entry["first_name"]
    last = entry["last_name"]
    password = entry["password"]
    email = entry["email"]

    user = User.objects.create_user(username=username, first_name=first, last_name=last, password=password, email=email)
    user.save()
    return user

def add_user_profile(dict):
    avatar = dict["avatar"]
    workplace = dict["workplace"]
    website = dict["website"]
    phone = dict["phone_number"]

    profile = UserProfile.objects.get_or_create(avatar=avatar, workplace=workplace, website=website, phone=phone)[0]
    profile.save()
    return profile

def add_comment(text, date):
    comment = Comment.objects.get_or_create(text=text, date=date)[0]
    comment.save()
    return comment

def add_post():
    post = Post.objects.get_or_create()[0]
    post.save()
    return post
