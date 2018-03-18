from django import forms
from tatu.models import *
from django.contrib.auth.models import User
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

# Base User Form to be instantiated by the login and register view
# Demands username, password, email, first and last names
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

# Expanded User Form to be instantiated by register
class ProfileForm(forms.ModelForm):
#    avatar = ProcessedImageField(spec_id='tatu:profile:avatar',
#                                 processors=[ResizeToFill(150, 150)],
#                                 format='JPEG',
#                                 options={'quality': 100})
#    website = forms.URLField(required=False)
#    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=False)

    class Meta:
        model = UserProfile
        fields = ('avatar', 'phone_number', 'website')
        exclude = ('user',)


