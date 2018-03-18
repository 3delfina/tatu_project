from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Page(models.Model):
    #user = models.ForeignKey(User)
    url = models.CharField(max_length=100)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
    

class UserProfile(models.Model):
    # This maps each UserProfile to have a field that inherits from the User Model
    # The User Model has username, password, email etc fields already associated with it
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # field for user avatar, defaults to /media/default/avatar.png
    avatar = ProcessedImageField(upload_to=user_directory_path,
                               processors=[ResizeToFill(150, 150)],
                               format='JPEG',
                               options={'quality': 100},
                               default='default/avatar.png')
    # Self Explanatory extraneous fields
    workplace = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$') 
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # for whenever a method in a view etc calls str() on this object
    def __str__(self):
        return self.user.username


# TATTOO MODEL WIP, PLEASE DONT TOUCH!

#class Tattoo(models.Model):
#    user = models.ForeignKey(User, related_name='images')
#    image = models.ImageField()
#    description = model.TextField()
#    tag = models.CharField(max_length=30)
#    rating = models.IntegerField()
#    favourites = models.IntegerField()


class Comment(models.Model):
    #user = models.ForeignKey(User)
    #picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

#class FavArtist(models.Model):
    #user = models.ForeignKey(User)
