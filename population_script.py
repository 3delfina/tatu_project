import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tatu_project.settings')

import django
django.setup()
from tatu.models import UserProfile, Post, Comment
from django.contrib.auth.models import User
import datetime
from imagekit.models import ProcessedImageField

## NOTE: RUN THE POPULATION SCRIPT FIRST, BEFORE YOU CREATE A NEW SUPERUSER ACCOUNT!

def populate():

    users = [
        {"username": "xo_g1ve_m3_h0p3_xo",
         "first_name": "Hannah",
         "last_name": "Spritz",
         "password": "teletubbies32",
         "email": "hannah.spritz@gmail.com"},
        {"username": "jezza32",
         "first_name": "John",
         "last_name": "Franco",
         "password": "password",
         "email": "jezza32@gmail.com"},
        {"username": "pizzagirl82",
         "first_name": "Sophie",
         "last_name": "O'Connelly",
         "password": "pizzaisthebest",
         "email": "pizzagirl82@gmail.com"},
        {"username": "bronzedidol",
         "first_name": "Katie",
         "last_name": "Mclaughlin",
         "password": "mypasswordisthebestpassword",
         "email": "bronzedidol@gmail.com"},
        {"username": "miss.sporty132",
         "first_name": "Emma",
         "last_name": "Barton",
         "password": "starwars3210",
         "email": "emma.barton.designs@gmail.com"},
        {"username": "solarsparkle",
         "first_name": "Ruaridh",
         "last_name": "O'Donahue",
         "password": "aaaaaaaaaaaa1278",
         "email": "solarsparkle@gmail.com"},
        {"username": "tattooking",
         "first_name": "Calum",
         "last_name": "Crawford",
         "password": "woohoo32!",
         "email": "tattooking@gmail.com"},
        {"username": "iHeartCookies",
         "first_name": "Jennifer",
         "last_name": "Armstrong",
         "password": "yeaboii_19",
         "email": "tattooqueen@gmail.com"},
        {"username": "ToTaLeClipse",
         "first_name": "Mark",
         "last_name": "Tweedie",
         "password": "chelseafc",
         "email": "totaleclipse@gmail.com"},
        {"username": "showstopper",
         "first_name": "Simon",
         "last_name": "Douglas",
         "password": "bubbles32",
         "email": "totaleclipse@gmail.com"},
    ]

    user_profiles = {
        "xo_g1ve_m3_h0p3_xo": {
            "workplace": "Tattoo Heaven",
            "website": "www.tattooheaven.com",
            "phone_number": "07783745929"
        },
        "jezza32": {
            "workplace": "Lucky Cat Tattoo",
            "website": "www.google.com",
            "phone_number": "07792825577"
        },
        "pizzagirl82": {
            "workplace": "Otzi Tattoos",
            "website": "www.otzitattoos.com",
            "phone_number": "07253012332"
        },
        "bronzedidol": {
            "workplace": "Otzi Tattoos",
            "website": "www.otzitattoos.com",
            "phone_number": "07253012332"
        },
        "miss.sporty132": {
            "workplace": "Creative Art Tattoo Studio",
            "website": "www.creativearttattoo.com",
            "phone_number": "01233748229"
        },
        "solarsparkle": {
            "workplace": "Timeless Tattoos",
            "website": "www.timelesstattoos.co.uk",
            "phone_number": "01342882291"
        },
        "tattooking": {
            "workplace": "Timeless Tattoos",
            "website": "www.timelesstattoos.co.uk",
            "phone_number": "01342882291"
        },
        "iHeartCookies": {
            "workplace": "Blancolo Tattoo",
            "website": "www.blancolotattoo.com",
            "phone_number": "01325672812"
        },
        "ToTaLeClipse": {
            "workplace": "Terry's Tattoo Studio",
            "website": "www.terrystattoostudio.com",
            "phone_number": "07839782557"
        },
        "showstopper": {
            "workplace": "Sugar Skull Tattoos",
            "website": "www.sugarskullglasgow.com",
            "phone_number": "08255667829"
        },
    }

# each set of posts is attributed to a specific user.
# each user has an associated list of posts they've created.
# ISSUE: need to work out how to allow for dates in the past - get round auto_now_add
    posts = {
        "xo_g1ve_m3_h0p3_xo": [
            {"category": "GM",
             "description": "aaa",
             "date": datetime.date(2018,3,12),
             "likes": 13,
             "filename": "gm1.jpg"},
            {"category": "BW",
             "description": "aaa",
             "date": datetime.date(2018,3,16),
             "likes": 17,
             "filename": "bw2.jpg"}
        ],
        "jezza32": [
            {"category": "RL",
             "description": "Perhaps the best tattoo I've ever completed! Ultra realistic.",
             "date": datetime.date(2018,3,16),
             "likes": 5,
             "filename": "rl1.jpg"},
            {"category": "WC",
             "description": "Perhaps the best tattoo I've ever completed! Ultra realistic.",
             "date": datetime.date(2018,3,3),
             "likes": 41,
             "filename": "wc3.jpg"}
        ],
        "pizzagirl82": [
            {"category": "BW",
             "description": "aaa",
             "date": datetime.date(2018,3,15),
             "likes": 2,
             "filename": "bw1.jpg"},
            {"category": "JP",
             "description": "aaa",
             "date": datetime.date(2018,3,5),
             "likes": 5,
             "filename": "jp1.jpg"},
            {"category": "GM",
             "description": "aaa",
             "date": datetime.date(2018,3,7),
             "likes": 19,
             "filename": "gm3.jpg"}
        ],
        "bronzedidol": [
            {"category": "WC",
             "description": "aaa",
             "date": datetime.date(2018,3,10),
             "likes": 21,
             "filename": "wc1.jpg"},
            {"category": "JP",
             "description": "aaa",
             "date": datetime.date(2018,3,11),
             "likes": 33,
             "filename": "jp3.jpg"},
            {"category": "TR",
             "description": "aaa",
             "date": datetime.date(2018,3,14),
             "likes": 19,
             "filename": "tr3.jpg"}
        ],
        "miss.sporty132": [
            {"category": "DW",
             "description": "aaa",
             "date": datetime.date(2018,3,16),
             "likes": 20,
             "filename": "dw1.jpg"}
        ],
        "solarsparkle": [
            {"category": "WC",
             "description": "aaa",
             "date": datetime.date(2018,3,8),
             "likes": 18,
             "filename": "wc2.jpg"},
            {"category": "TD",
             "description": "aaa",
             "date": datetime.date(2018,3,21),
             "likes": 16,
             "filename": "td1.jpg"},
            {"category": "TD",
             "description": "aaa",
             "date": datetime.date(2018,3,21),
             "likes": 6,
             "filename": "td3.jpg"},
            {"category": "RL",
             "description": "aaa",
             "date": datetime.date(2018,3,1),
             "likes": 4,
             "filename": "rl3.jpg"},
            {"category": "LT",
             "description": "aaa",
             "date": datetime.date(2018,3,2),
             "likes": 35,
             "filename": "lt2.jpg"},
            {"category": "LT",
             "description": "aaa",
             "date": datetime.date(2018,3,2),
             "likes": 34,
             "filename": "lt3.jpg"}
        ],
        "tattooking": [
            {"category": "TR",
             "description": "aaa",
             "date": datetime.date(2018,3,13),
             "likes": 5,
             "filename": "tr1.jpg"},
            {"category": "TD",
             "description": "aaa",
             "date": datetime.date(2018,3,6),
             "likes": 7,
             "filename": "td2.jpg"},
            {"category": "LT",
             "description": "aaa",
             "date": datetime.date(2018,3,2),
             "likes": 11,
             "filename": "lt1.jpg"},
        ],
        "iHeartCookies": [
            {"category": "GM",
             "description": "aaa",
             "date": datetime.date(2018,3,1),
             "likes": 7,
             "filename": "gm2.jpg"}
        ],
        "ToTaLeClipse": [
            {"category": "TR",
             "description": "aaa",
             "date": datetime.date(2018,3,18),
             "likes": 32,
             "filename": "tr2.jpg"},
            {"category": "RL",
             "description": "aaa",
             "date": datetime.date(2018,2,25),
             "likes": 19,
             "filename": "rl2.jpg"},
            {"category": "JP",
             "description": "aaa",
             "date": datetime.date(2018,2,20),
             "likes": 19,
             "filename": "jp2.jpg"}
        ],
        "showstopper": [
            {"category": "TD",
             "description": "One of my works from when I first started out. I had uh...room for improvement.",
             "date": datetime.date(2018,3,19),
             "likes": 64,
             "filename": "td4.jpg"},
            {"category": "DW",
             "description": "aaa",
             "date": datetime.date(2018,3,22),
             "likes": 47,
             "filename": "dw2.jpg"},
            {"category": "DW",
             "description": "aaa",
             "date": datetime.date(2018,3,19),
             "likes": 38,
             "filename": "dw3.jpg"},
            {"category": "BW",
             "description": "aaa",
             "date": datetime.date(2018,3,13),
             "likes": 12,
             "filename": "bw3.jpg"}

        ],
    }

    comments = [
        {"text": "this tattoo sucks. die",
         "date": datetime.date(2018,3,20),
         "username": "jezza32",
         "post_id": 3},
        {"text": "This work is amazing! You should be proud!",
         "date": datetime.date(2018,3,19),
         "username": "xo_g1ve_m3_h0p3_xo",
         "post_id": 1},
        {"text": "uhm. it's interesting",
         "date": datetime.date(2018,3,17),
         "username": "pizzagirl82",
         "post_id": 2}
    ]

    for ix, user_info in enumerate(users):
        user = add_user(user_info)
        username = user.get_username()
        profile = add_user_profile(user, user_profiles[username])
        for post_info in posts[username]:
            add_post(user, post_info)

    for comment in comments:
        add_comment(comment)

def add_user(entry):
    user = User.objects.create_user(username=entry["username"],
                                    first_name=entry["first_name"],
                                    last_name=entry["last_name"],
                                    password=entry["password"],
                                    email=entry["password"])
    user.save()
    return user

def add_user_profile(user, dict):
    username = user.username
    avatar = os.path.join(username, 'avatar', "profile.jpg")
    profile = UserProfile.objects.get_or_create(user=user,
                                                avatar=avatar,
                                                workplace=dict["workplace"],
                                                website=dict["website"],
                                                phone_number=dict["phone_number"])[0]
    profile.save()
    return profile

def add_post(user, dict):
    username = user.username
    image = os.path.join(username, 'posts', dict["filename"])
    post = Post.objects.get_or_create(author=user,
                                      category=dict["category"],
                                      image=image,
                                      description=dict["description"],
                                      date=dict["date"],
                                      likes=dict["likes"])[0]
    post.save()
    return post

def add_comment(info):
    user = User.objects.get(username=info["username"])
    user_profile = UserProfile.objects.get(user=user)
    post = Post.objects.get(id=info["post_id"])

    # ISSUE: why is the tuple necessary? get_or_create returns tuple, but isn't problematic elsewhere
    # ISSUE: must add date to get_or_create function - override auto_add_now in DateTimeField
    comment, aaa = Comment.objects.get_or_create(thread=post,
                                                 poster=user_profile,
                                                 text=info["text"])
    comment.save()
    return comment

if __name__ == '__main__':
    print("Starting Tatu population script...")
    populate()