from django import forms
from ..models import PreparedQuestion


class PreparedQuestionForm(forms.ModelForm):
    class Meta:
        model = PreparedQuestion
        fields = ['title', 'content']
