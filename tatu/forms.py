from django import forms
from tatu.models import *
from django.contrib.auth.models import User
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'comment-text', 
                'required': True, 
                'placeholder': 'What do you think...'
            }),
		}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'category', 'description')

# Base User Form to be instantiated by the login and register view
# Demands username, password, email, first and last names
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput()) 
    
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email', 'first_name', 'last_name')
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirmation password do not match!"
            )


# Expanded User Form to be instantiated by register
class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar', 'phone_number', 'website')
        exclude = ('user', 'favourites')

class ContactForm(forms.Form):
    your_name = forms.CharField(required=True)
    your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
