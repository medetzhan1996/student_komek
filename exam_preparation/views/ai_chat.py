from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import View
from django.http import JsonResponse

from ..models import AIGenerated
from ..forms import AIChatForm
from ..service import generate_ai_chat
from ..constant import CHAT


class AIChatListView(LoginRequiredMixin, ListView):
    model = AIGenerated
    context_object_name = 'ai_chats'
    template_name = 'exam_preparation/ai_chat/list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(
            kind=CHAT
        ).filter_by_user(
            user_id=user.id
        )
        return queryset


class AIChatCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        form = AIChatForm(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            ai_question = generate_ai_chat(text)
            if text and ai_question:
                AIGenerated.objects.create(
                    request=text,
                    response=ai_question,
                    user=user,
                    kind=CHAT
                )
            return JsonResponse({
                'request': text,
                'response': ai_question
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)