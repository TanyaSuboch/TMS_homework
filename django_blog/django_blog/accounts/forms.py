from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .models import User, Reader, Author


class ReaderSignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First name:', required=True)
    last_name = forms.CharField(label='Last name:', required=True)
    email = forms.EmailField(label='E-mail:', required=True)
    country = forms.CharField(label='Country:', required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    @csrf_exempt
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        reader = Reader.objects.create(user=user)
        reader.country = self.cleaned_data.get('country')
        reader.save()
        return user


class AuthorSignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First name:', required=True)
    last_name = forms.CharField(label='Last name:', required=True)
    email = forms.EmailField(label='E-mail:', required=True)
    activity = forms.CharField(label='Activity:', required=True)
    company = forms.CharField(label='Company:', required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    @csrf_exempt
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        author = Author.objects.create(user=user)
        author.activity = self.cleaned_data.get('activity')
        author.company = self.cleaned_data.get('company')
        author.save()
        return user