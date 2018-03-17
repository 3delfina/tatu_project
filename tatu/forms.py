from django import forms
from tatu.models import *
from django.contrib.auth.models import User
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields('username', 'password', 'email', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    avatar = ProcessedImageField(spec_id='tatu:profile:avatar',
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 100},
                                 required=False)
    website = forms.URLField(required=False)
    phone_number = forms.RegexField(required=False)

    class Meta:
        model = UserProfile
        fields = ('avatar', 'phone_number', 'website')
        exclude = ('user',)


