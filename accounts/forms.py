from django import forms
from django.contrib.auth.password_validation import validate_password
from django.forms import ModelForm

from .models import MyUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser

        fields = ["first_name", "last_name", "middle_name", "address", "email", "password"]

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "middle_name": "Middle Name",
            "email": "Email",
            "address": "Address",
            "password": "Password",
        }

        help_text = {
            "password": "Include numbers for better security",
        }

        error_messages = {
            "full_name": {"required": "you must enter your name"},
            "address": {"required": "You must provide a valid address"},
            "password": {"required": "You must enter your password"},
            "email": {"required": "Email required for verification"},
        }

