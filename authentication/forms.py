from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from authentication.models import Proposal

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    profession = forms.CharField(max_length=180)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'profession']


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['full_name', 'phone_number', 'profession']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
