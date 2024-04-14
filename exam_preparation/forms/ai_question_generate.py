from django import forms


class AIQuestionQenerateForm(forms.Form):
    text = forms.CharField(
        max_length=1500
    )
