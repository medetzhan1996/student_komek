from django import forms

from ..models import AIGenerated


class AIGeneratedForm(forms.ModelForm):
    class Meta:
        model = AIGenerated
        fields = ['request', 'response']
