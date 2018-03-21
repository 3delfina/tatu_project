import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tatu_project.settings')

import django
django.setup()
from tatu.models import UserProfile, Post, Comment
from django.contrib.auth.models import User
import datetime

# UserProfile (avatar, workplace, website, phone_number)
# Post (category, author, image, description, date, favourites)
# Comment (text, date)

# instance: if the user's id is 13, their avatar will be saved to:
# .../tatu_project/media/user_13/avatar/(filename)

def pop_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # change this to the path pages are saved at
    return 'user_{0}/avatar/{1}'.format(instance.user.id, filename)

def populate():

# what's the best way to map users to user_profiles?

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
         "email": "pizzaboy82@gmail.com"}
    ]

    user_profiles = {
        "jezza32": {
            "avatar": "Users/rossclark/workspace/pop/a",
            "workplace": "Tattoo Heaven",
            "website": "www.tattooheaven.com",
            "phone_number": "07783745929"
        },
        "xo_g1ve_m3_h0p3_xo": {
            "avatar": "Users/rossclark/workspace/pop/b",
            "workplace": "Lucky Cat Tattoo",
            "website": "www.google.com",
            "phone_number": "07792825577"
        },
        "pizzaboy82": {
            "avatar": "Users/rossclark/workspace/pop/c",
            "workplace": "Otzi Tattoos",
            "website": "www.otzitattoos.com",
            "phone_number": "07783745929"
        }
    }

# each set of posts is attributed to a specific user.
# each user has an associated list of posts they've created.
# ISSUE: need to work out how to allow for dates in the past - get round auto_now_add
    posts = {
        "jezza32": [
            {"category": "RL",
             "image": "Users/rossclark/workspace/pop/a",
             "description": "Perhaps the best tattoo I've ever completed! Ultra realistic.",
             "date": datetime.date(2018,3,16),
             "likes": 5}
        ],
        "xo_g1ve_m3_h0p3_xo": [
            {"category": "GM",
             "image": "Users/rossclark/workspace/pop/b",
             "description": "aaa",
             "date": datetime.date(2018,3,12),
             "likes": 13}
        ],
        "pizzaboy82": [
            {"category": "BW",
             "image": "Users/rossclark/workspace/pop/c",
             "description": "aaa",
             "date": datetime.date(2018,3,15),
             "likes": 2}
        ]
    }

# comments are associated with individual posts as well as individual users (posters)
# need to alter below code so as to allow for that
# ISSUE: need to work out how to allow for dates in the past - get round auto_now_add
    comments = {
        "jezza32": [
            {"text": "this tattoo sucks. die",
             "date": datetime.date(2018,3,20),
             "post_id": 3}
        ],
        "xo_g1ve_m3_h0p3_xo": [
            {"text": "This work is amazing! You should be proud!",
             "date": datetime.date(2018,3,19),
             "post_id": 1}
        ],
        "pizzaboy82": [
            {"text": "uhm. it's interesting",
             "date": datetime.date(2018,3,17),
             "post_id": 2}
        ]
    }

    for ix, user_info in enumerate(users):
        user = add_user(user_info)
        username = user.get_username()
        profile = add_user_profile(user, user_profiles[username])
        for post_info in posts[username]:
            add_post(user, post_info)

    for username, comment_info in comments.items():
        for comment in comment_info:
            add_comment(username, comment)


# we use the username attribute to identify unique users
# we use the post id (?) to identify unique posts

def add_user(entry):
    user = User.objects.create_user(username=entry["username"],
                                    first_name=entry["first_name"],
                                    last_name=entry["last_name"],
                                    password=entry["password"],
                                    email=entry["password"])
    user.save()
    return user

def add_user_profile(user, dict):
    profile = UserProfile.objects.get_or_create(user=user,
                                                avatar=dict["avatar"],
                                                workplace=dict["workplace"],
                                                website=dict["website"],
                                                phone_number=dict["phone_number"])[0]
    profile.save()
    return profile

def add_post(user, dict):
    post = Post.objects.get_or_create(author=user,
                                      category=dict["category"],
                                      image=dict["image"],
                                      description=dict["description"],
                                      date=dict["date"],
                                      likes=dict["likes"])[0]
    post.save()
    return post

def add_comment(username, info):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    post = Post.objects.get(id=info["post_id"])

    # ISSUE: why is this necessary? get_or_create returns tuple, but isn't problematic elsewhere
    comment, aaa = Comment.objects.get_or_create(thread=post,
                                            poster=user_profile,
                                            text=info["text"])
    comment.save()
    return comment
    # ISSUE: need to add date to constructor

if __name__ == '__main__':
    print("Starting Tatu population script...")
    populate()
