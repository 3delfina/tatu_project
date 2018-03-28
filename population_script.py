import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tatu_project.settings')

import django
django.setup()
import datetime
from django.contrib.auth.models import User
from tatu.models import UserProfile, Post, Comment, Like
from django.core.files.uploadedfile import SimpleUploadedFile

MEDIA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')

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
# ISSUE: remember to sort the dates!

    posts = {
        "xo_g1ve_m3_h0p3_xo": [
            {"category": "GM",
             "description": "Geometric nature",
             "date": datetime.date(2018,2,12),
             "filename": "gm1.jpg"},
            {"category": "BW",
             "description": "Blackwork heart",
             "date": datetime.date(2018,2,16),
             "filename": "bw2.jpg"},
            {"category": "TD",
             "description": "Compass",
             "date": datetime.date(2018,2,16),
             "filename": "td5.jpg"},
            {"category": "TD",
             "description": "",
             "date": datetime.date(2018,2,16),
             "filename": "td6.jpg"},
        ],
        "jezza32": [
            {"category": "RL",
             "description": "Zeus. Super proud of this one.",
             "date": datetime.date(2018,2,16),
             "filename": "rl1.jpg"},
            {"category": "WC",
             "description": "Galactic diamond",
             "date": datetime.date(2018,2,3),
             "filename": "wc3.jpg"},
            {"category": "RL",
             "description": "",
             "date": datetime.date(2018,2,3),
             "filename": "rl4.jpg"}
        ],
        "pizzagirl82": [
            {"category": "BW",
             "description": "Intricate dragon design",
             "date": datetime.date(2018,2,15),
             "filename": "bw1.jpg"},
            {"category": "JP",
             "description": "Koi tattoo",
             "date": datetime.date(2018,2,5),
             "filename": "jp1.jpg"},
            {"category": "GM",
             "description": "A very geometric mountainside",
             "date": datetime.date(2018,2,7),
             "filename": "gm3.jpg"},
            {"category": "RL",
             "description": "Hyper-realistic eye",
             "date": datetime.date(2018,2,3),
             "filename": "rl5.jpg"},
            {"category": "WC",
             "description": "beautiful fox",
             "date": datetime.date(2018, 2, 3),
             "filename": "wc4.jpg"}
        ],
        "bronzedidol": [
            {"category": "WC",
             "description": "Watercolour birds",
             "date": datetime.date(2018,2,10),
             "filename": "wc1.jpg"},
            {"category": "JP",
             "description": "Dragon tattoo on torso",
             "date": datetime.date(2018,2,11),
             "filename": "jp3.jpg"},
            {"category": "TR",
             "description": "",
             "date": datetime.date(2018,2,14),
             "filename": "tr3.jpg"},
            {"category": "RL",
             "description": "",
             "date": datetime.date(2018,2,3),
             "filename": "rl6.jpg"}
        ],
        "miss.sporty132": [
            {"category": "DW",
             "description": "Veeery intricate dotwork!",
             "date": datetime.date(2018,2,16),
             "filename": "dw1.jpg"},
            {"category": "WC",
             "description": "watercolour flower",
             "date": datetime.date(2018, 2, 3),
             "filename": "wc6.jpg"},
            {"category": "DW",
             "description": "spotty starry sky",
             "date": datetime.date(2018, 2, 3),
             "filename": "dw4.jpg"}
        ],
        "solarsparkle": [
            {"category": "WC",
             "description": "Leaping fox",
             "date": datetime.date(2018,2,8),
             "filename": "wc2.jpg"},
            {"category": "TD",
             "description": "Spooky",
             "date": datetime.date(2018,2,21),
             "filename": "td1.jpg"},
            {"category": "TD",
             "description": "Every path leads home",
             "date": datetime.date(2018,2,21),
             "filename": "td3.jpg"},
            {"category": "RL",
             "description": "My most realistic animal tattoo to date!",
             "date": datetime.date(2018,2,1),
             "filename": "rl3.jpg"},
            {"category": "LT",
             "description": "beautiful",
             "date": datetime.date(2018,2,2),
             "filename": "lt2.jpg"},
            {"category": "LT",
             "description": "no future",
             "date": datetime.date(2018,2,2),
             "filename": "lt3.jpg"},
            {"category": "WC",
             "description": "Crashing waves",
             "date": datetime.date(2018, 2, 3),
             "filename": "wc5.jpg"}
        ],
        "tattooking": [
            {"category": "TR",
             "description": "First tribal tattoo",
             "date": datetime.date(2018,2,13),
             "filename": "tr1.jpg"},
            {"category": "TD",
             "description": "Had a whale of a time with this one",
             "date": datetime.date(2018,2,6),
             "filename": "td2.jpg"},
            {"category": "LT",
             "description": "blessed",
             "date": datetime.date(2018,2,2),
             "filename": "lt1.jpg"},
            {"category": "DW",
             "description": "dotwork skull",
             "date": datetime.date(2018, 2, 3),
             "filename": "dw5.jpg"},
            {"category": "BW",
             "description": "",
             "date": datetime.date(2018, 2, 3),
             "filename": "bw5.jpg"}
        ],
        "iHeartCookies": [
            {"category": "GM",
             "description": "Minimalist geometric tattoo",
             "date": datetime.date(2018,2,1),
             "filename": "gm2.jpg"},
            {"category": "DW",
             "description": "dotwork wave",
             "date": datetime.date(2018, 2, 3),
             "filename": "dw6.jpg"},
            {"category": "BW",
             "description": "dark roses",
             "date": datetime.date(2018, 2, 3),
             "filename": "bw4.jpg"}
        ],
        "ToTaLeClipse": [
            {"category": "TR",
             "description": "Tribal",
             "date": datetime.date(2018,2,18),
             "filename": "tr2.jpg"},
            {"category": "RL",
             "description": "Hyper-realistic eye tattoo",
             "date": datetime.date(2018,2,25),
             "filename": "rl2.jpg"},
            {"category": "JP",
             "description": "Japanese castle",
             "date": datetime.date(2018,2,20),
             "filename": "jp2.jpg"},
            {"category": "GM",
             "description": "",
             "date": datetime.date(2018, 2, 3),
             "filename": "gm5.jpg"},
            {"category": "GM",
             "description": "geometric elephant",
             "date": datetime.date(2018, 2, 3),
             "filename": "gm6.jpg"}
        ],
        "showstopper": [
            {"category": "TD",
             "description": "One of my works from when I first started out. It had...room for improvement.",
             "date": datetime.date(2018,2,19),
             "filename": "td4.jpg"},
            {"category": "DW",
             "description": "Dotwork spiral",
             "date": datetime.date(2018,2,22),
             "filename": "dw2.jpg"},
            {"category": "DW",
             "description": "Dotwork band",
             "date": datetime.date(2018,2,19),
             "filename": "dw3.jpg"},
            {"category": "BW",
             "description": "Blackwork spiral",
             "date": datetime.date(2018,2,13),
             "filename": "bw3.jpg"},
            {"category": "BW",
             "description": "skull in a bottle",
             "date": datetime.date(2018, 2, 3),
             "filename": "bw6.jpg"},
            {"category": "GM",
             "description": "minimalist",
             "date": datetime.date(2018, 2, 3),
             "filename": "gm4.jpg"}
        ],
    }

    comments = [
        {"text": "this tattoo sucks. die",
         "date": datetime.date(2018,3,20),
         "username": "showstopper",
         "post_id": 3},
        {"text": "This work is amazing! You should be proud!",
         "date": datetime.date(2018,3,19),
         "username": "showstopper",
         "post_id": 1},
        {"text": "uhm. it's interesting",
         "date": datetime.date(2018,3,17),
         "username": "pizzagirl82",
         "post_id": 2},
        {"text": "If you had done this to me I'd have sued.",
         "date": datetime.date(2018,3,12),
         "username": "jezza32",
         "post_id": 40},
        {"text": "holy christ",
         "date": datetime.date(2018, 3, 12),
         "username": "tattooking",
         "post_id": 40},
        {"text": "this is worse than what Cheney did to Iraq",
         "date": datetime.date(2018, 3, 12),
         "username": "bronzedidol",
         "post_id": 40},
        {"text": "seriously beautiful! this piece must have taken forever to complete.",
         "date": datetime.date(2018, 3, 12),
         "username": "miss.sporty132",
         "post_id": 9},
        {"text": "This is a very intricate piece of work. Really impressive.",
         "date": datetime.date(2018, 3, 12),
         "username": "ToTaLeClipse",
         "post_id": 5},
        {"text": "This is a beautifully minimalist piece of work.",
         "date": datetime.date(2018, 3, 12),
         "username": "xo_g1ve_m3_h0p3_xo",
         "post_id": 21},
        {"text": "i'm obsessed with this tattoo. really well done!",
         "date": datetime.date(2018, 3, 12),
         "username": "showstopper",
         "post_id": 12},
        {"text": "this is a masterpiece. properly impressive!",
         "date": datetime.date(2018, 3, 12),
         "username": "jezza32",
         "post_id": 15},
        {"text": "The use of colour is really lovely in this. Thanks for sharing!",
         "date": datetime.date(2018, 3, 12),
         "username": "bronzedidol",
         "post_id": 19},
        {"text": "This has got to be one of the most realistic tattoos I've ever seen. Seriously, bravo.",
         "date": datetime.date(2018, 3, 12),
         "username": "pizzagirl82",
         "post_id": 23},
        {"text": "Simple but effective. Really great job",
         "date": datetime.date(2018, 3, 12),
         "username": "iHeartCookies",
         "post_id": 28},
        {"text": "Really professionally done! Nice one.",
         "date": datetime.date(2018, 3, 12),
         "username": "solarsparkle",
         "post_id": 27},
        {"text": "Couldn't put it any better than the tattoo itself!",
         "date": datetime.date(2018, 3, 12),
         "username": "solarsparkle",
         "post_id": 16},
        {"text": "Wow, beautiful. Where did you get the inspiration for this?",
         "date": datetime.date(2018, 3, 12),
         "username": "tattooking",
         "post_id": 6},
    ]

    likes = [
        {"liker": "solarsparkle", "post_id": 1},
        {"liker": "ToTaLeClipse", "post_id": 3},
        {"liker": "bronzedidol", "post_id": 3},
        {"liker": "miss.sporty132", "post_id": 4},
        {"liker": "showstopper", "post_id": 4},
        {"liker": "iHeartCookies", "post_id": 4},
        {"liker": "jezza32", "post_id": 6},
        {"liker": "xo_g1ve_m3_h0p3_xo", "post_id": 6},
        {"liker": "tattooking", "post_id": 7},
        {"liker": "pizzagirl82", "post_id": 8},
        {"liker": "solarsparkle", "post_id": 9},
        {"liker": "iHeartCookies", "post_id": 10},
        {"liker": "ToTaLeClipse", "post_id": 12},
        {"liker": "bronzedidol", "post_id": 12},
        {"liker": "iHeartCookies", "post_id": 12},
        {"liker": "pizzagirl82", "post_id": 14},
        {"liker": "jezza32", "post_id": 20},
        {"liker": "iHeartCookies", "post_id": 22},
        {"liker": "solarsparkle", "post_id": 22},
        {"liker": "solarsparkle", "post_id": 26},
        {"liker": "pizzagirl82", "post_id": 27},
    ]

    for ix, user_info in enumerate(users):
        user = add_user(user_info)
        username = user.get_username()
        add_user_profile(user, user_profiles[username])
        for post_info in posts[username]:
            post = add_post(user, post_info)

    for comment in comments:
        add_comment(comment)

    for like in likes:
        add_like(like)

    # this sets the number of likes for a post = number of like objects registered to the post
    for post in Post.objects.all():
        post.likes = Like.objects.filter(post=post).count()
        post.save()

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
    path = os.path.join('pop', 'avis', username+'.jpg')
    # path now stores <MEDIA_DIR>/pop/avis/<username>.jpg
    image = SimpleUploadedFile(name='avatar.jpg',
                               content=open(os.path.join(MEDIA_DIR, path), 'rb').read(),
                               content_type='image/jpeg')
    profile = UserProfile.objects.get_or_create(user=user,
                                                avatar=image,
                                                workplace=dict["workplace"],
                                                website=dict["website"],
                                                phone_number=dict["phone_number"])[0]
    profile.save()
    return profile

def add_post(user, dict):
    path = os.path.join('pop', 'tats', dict["category"], dict["filename"])
    # path now stores <MEDIA_DIR>/pop/tats/<category>/<filename>
    # note that the filename already has .jpg attached to the end
    image = SimpleUploadedFile(name=dict["filename"],
                               content=open(os.path.join(MEDIA_DIR, path), 'rb').read(),
                               content_type='image/jpeg')
    post = Post.objects.get_or_create(author=user,
                                      category=dict["category"],
                                      image=image,
                                      description=dict["description"],
                                      date=dict["date"],
                                      #likes=dict["likes"])[0]
                                      )[0]
    post.save()
    return post

def add_comment(info):
    user = User.objects.get(username=info["username"])
    user_profile = UserProfile.objects.get(user=user)
    post = Post.objects.get(id=info["post_id"])

    # ISSUE: must add date to get_or_create function - override auto_add_now in DateTimeField
    comment, aaa = Comment.objects.get_or_create(thread=post,
                                                 poster=user_profile,
                                                 text=info["text"])
    comment.save()
    return comment

def add_like(info):
    user = User.objects.get(username=info['liker'])
    post = Post.objects.get(id=info['post_id'])
    like, aaa = Like.objects.get_or_create(user=user, post=post)
    like.save()
    return like


if __name__ == '__main__':
    print("Running Tatu population script...")
    populate()