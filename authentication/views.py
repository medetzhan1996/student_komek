from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from authentication.forms import CustomUserCreationForm


class UserRegistrationView(CreateView):
    template_name = 'authentication/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


class ConfirmationPageView(TemplateView):
    template_name = 'authentication/confirmation_page.html'
