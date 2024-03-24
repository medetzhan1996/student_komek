from django import forms


class AIChatForm(forms.Form):
    text = forms.CharField(
        max_length=200
    )
