from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Photo

# User registration form with email field
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # Validate unique username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken")
        return username

    # Validate unique email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use")
        return email

# Form for photo uploads
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

    # Validate image file
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check file size (max 5MB)
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("File size is too big")
            # Check file extension
            if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError("Only JPG/PNG images are allowed")
            return image