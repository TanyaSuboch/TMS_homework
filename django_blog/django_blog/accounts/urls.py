from django.urls import path
from accounts import views
from .views import ReaderSignUpView, AuthorSignUpView


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_reader/', ReaderSignUpView.as_view(), name='signup_reader'),
    path('signup_author/', AuthorSignUpView.as_view(), name='signup_author'),
]