from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.db import transaction

from .models import UserProfile


User = get_user_model()


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=120)
    email = forms.EmailField(max_length=254)
    company_name = forms.CharField(max_length=120, required=False)
    focus = forms.ChoiceField(choices=UserProfile.FOCUS_CHOICES)
    wants_pro_updates = forms.BooleanField(required=False, initial=True)
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")
        return cleaned_data

    @transaction.atomic
    def save(self):
        email = self.cleaned_data["email"]
        user = User.objects.create_user(
            username=email,
            email=email,
            password=self.cleaned_data["password1"],
            first_name=self.cleaned_data["full_name"].strip(),
        )
        profile = user.profile
        profile.company_name = self.cleaned_data["company_name"].strip()
        profile.focus = self.cleaned_data["focus"]
        profile.wants_pro_updates = self.cleaned_data["wants_pro_updates"]
        profile.save()
        return user


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, request=None, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email", "").strip().lower()
        password = cleaned_data.get("password")
        if email and password:
            self.user = authenticate(self.request, username=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Incorrect email or password.")
        return cleaned_data

    def get_user(self):
        return self.user


class ProfileForm(forms.Form):
    full_name = forms.CharField(max_length=120)
    company_name = forms.CharField(max_length=120, required=False)
    focus = forms.ChoiceField(choices=UserProfile.FOCUS_CHOICES)
    wants_pro_updates = forms.BooleanField(required=False)

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        if user and not self.is_bound:
            self.initial = {
                "full_name": user.first_name,
                "company_name": user.profile.company_name,
                "focus": user.profile.focus,
                "wants_pro_updates": user.profile.wants_pro_updates,
            }
            for key, value in self.initial.items():
                self.fields[key].initial = value

    @transaction.atomic
    def save(self):
        self.user.first_name = self.cleaned_data["full_name"].strip()
        self.user.save(update_fields=["first_name"])
        profile = self.user.profile
        profile.company_name = self.cleaned_data["company_name"].strip()
        profile.focus = self.cleaned_data["focus"]
        profile.wants_pro_updates = self.cleaned_data["wants_pro_updates"]
        profile.save()
        return self.user
