from django.db import models
from django.contrib.auth.models import User
from uuid import UUID

#class Category(models.Model):
#    name = models.CharField(max_length=128, unique=True)
#    views = models.IntegerField(default=0)
#    likes = models.IntegerField(default=0)
#    slug = models.SlugField(unique=True)

#    def save(self, *args, **kwargs):
#        self.slug = slugify(self.name)
#        super(Category, self).save(*args, **kwargs)

#    class Meta:
#        verbose_name_plural = 'categories'

#    def __str__(self):
#        return self.name


#class Page(models.Model):
#    category = models.ForeignKey(Category)
#    title = models.CharField(max_length=128)
#    url = models.URLField()
#    views = models.IntegerField(default=0)

#    def __str__(self):
#        return self.title

#class UserProfile(models.Model):
#    user = models.OneToOneField(User)
#    website = models.URLField(blank=True)
#    picture = models.ImageField(upload_to="profile_images", blank=True)
#    
#    def __str__(self):
#        return self.user.username

# IDs are automatically used according to django docs, so no need to add id fields manually

class Page(models.Model):
    #user = models.ForeignKey(User)
    url = models.CharField(max_length=100)
    
class UserProfile(models.Model):
    fullname = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30) #(does password belong here?)
    picture = models.ImageField(blank=True)
    workplace = models.CharField(max_length=100, blank=True)
    phone_no = models.IntegerField(blank=True)
    website = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=30, blank=True)

    #def __str__(self):
        #return self.user.username #(?)

class UserImage(models.Model):
    tattoos = models.ForeignKey(UserProfile, 
                                related_name='images', 
                                on_delete=models.DO_NOTHING,
                                )
    image = models.ImageField()

class Picture(models.Model):
    #user = models.ForeignKey(User)
    tattoo_picture = models.ImageField()
    tag = models.CharField(max_length=30)
    rating = models.IntegerField()

class Comment(models.Model):
    #user = models.ForeignKey(User)
    #picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

#class FavArtist(models.Model):
    #user = models.ForeignKey(User)
