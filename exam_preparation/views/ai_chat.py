from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..models import AIChat


class AIChatListView(LoginRequiredMixin, ListView):
    model = AIChat
    context_object_name = 'ai_chats'
    template_name = 'exam_preparation/ai_chat/list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter_by_user(user_id=user.id)
        return queryset