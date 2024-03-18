from django.urls import path
from .views import UserRegistrationView, UserLoginView, ConfirmationPageView

app_name = 'authentication'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('confirmation/', ConfirmationPageView.as_view(), name='confirmation_page'),
]
