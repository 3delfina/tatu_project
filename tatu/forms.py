from django import forms
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class ProfileForm(forms.Form):
    avatar = ProcessedImageField(spec_id='tatu:profile:avatar',
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 100})

