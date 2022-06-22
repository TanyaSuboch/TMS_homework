from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView

from accounts.forms import AuthorSignUpForm, ReaderSignUpForm
from .models import User, Reader, Author


def signup(request):
    return render(request, 'signup_page.html')


class ReaderSignUpView(CreateView):
    model = User
    form_class = ReaderSignUpForm
    template_name = 'signup_reader.html'
    success_url = reverse_lazy('login')


class AuthorSignUpView(CreateView):
    model = User
    form_class = AuthorSignUpForm
    template_name = 'signup_author.html'
    success_url = reverse_lazy('login')