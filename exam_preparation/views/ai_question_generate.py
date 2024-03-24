from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from ..forms.ai_question_generate import AIQuestionQenerateForm
from ..service import generate_ai_question

class GetAiQuestion(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        form = AIQuestionQenerateForm(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            ai_question = generate_ai_question(text)
            return JsonResponse({'ai_question': ai_question})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
