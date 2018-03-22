import os
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings


def user_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return os.path.join(instance.user.username, 'avatar', filename)

def user_image_path(instance, filename):
    return os.path.join(instance.author.username, 'posts', filename)

class UserProfile(models.Model):
    # This maps each UserProfile to have a field that inherits from the User Model
    # The User Model has username, password, email etc fields already associated with it
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # field for user avatar, defaults to /media/default/avatar.png
    avatar = ProcessedImageField(upload_to=user_avatar_path,
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 100},
                                 default='default/avatar.png',
                                 blank=True)

    # Self Explanatory extraneous fields
    workplace = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$') 
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # for whenever a method in a view etc calls str() on this object
    def __str__(self):
        return self.user.username


# The Post model: Every post must have an image, description, number of likes
#                 and many posts may belong to only one Category and one User
class Post(models.Model):
    # The 'TD' etc are how the names will appear in the database
    TRADITIONAL = 'TD'
    REALISM = 'RL'
    WATERCOLOR = 'WC'
    TRIBAL = 'TR'
    DOTWORK = 'DW'
    GEOMETRIC = 'GM'
    JAPANESE = 'JP'
    LETTERING = 'LT'
    BLACKWORK = 'BW'
    
    # This enum links the short versions to the human readable ones
    CATEGORIES = (
        (TRADITIONAL, 'Traditional'),
        (REALISM, 'Realism'),
        (WATERCOLOR, 'Watercolor'),
        (TRIBAL, 'Tribal'),
        (DOTWORK, 'Dotwork'),
        (GEOMETRIC, 'Geometric'),
        (JAPANESE, 'Japanese'),
        (LETTERING, 'Lettering'),
        (BLACKWORK, 'Blackwork'),
    )

    category = models.CharField(max_length=2,
                            choices=CATEGORIES,
                            default=JAPANESE,
                            )

    # ManyToOne relationship: Many posts can be created by one User
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author',
                               default='admin'

                               )
    image = ProcessedImageField(upload_to=user_image_path,
                                processors=[ResizeToFill(1000, 1000)],
                                format='JPEG',
                                options={'quality': 90},
                                )
    
    description = models.CharField(max_length=280)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return "(#{0}) {1}: {2}".format(self.id, self.author.username, self.description[0:120])


# The Comment model: Every comment must have an author, text, date, and
#                    many comments may belong to only one Post and many
#                    comments can be posted by one user
class Comment(models.Model):
    thread = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             )
    poster = models.ForeignKey(UserProfile,
                               on_delete=models.CASCADE,
                               related_name='posters',
                               )

    text = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "#{0} - {1}".format(self.id, self.text[0:30])
