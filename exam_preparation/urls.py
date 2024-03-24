from django.urls import path
from .views import (
    PreparedQuestionCreateView,
    PreparedQuestionListView,
    PreparedQuestionDeleteView,
    PreparedQuestionUpdateView,
    PreparedQuestionDetailView,
    GetAiQuestion,
    AIChatListView,
    AIChatCreateView,
)

app_name = 'exam_preparation'

urlpatterns = [
    path('list/', PreparedQuestionListView.as_view(), name='prepared-question-list'),
    path('create/', PreparedQuestionCreateView.as_view(), name='prepared-question-create'),
    path('<int:pk>/delete/', PreparedQuestionDeleteView.as_view(), name='prepared-question-delete'),
    path('<int:pk>/edit/', PreparedQuestionUpdateView.as_view(), name='prepared-question-edit'),
    path('<int:pk>/detail/', PreparedQuestionDetailView.as_view(), name='prepared-question-detail'),

    path('get-ai-question/', GetAiQuestion.as_view(), name='get-ai-question'),
    path('ai-chat/', AIChatListView.as_view(), name='ai-chat'),
    path('ai-chat-create/', AIChatCreateView.as_view(), name='ai-chat-create'),

]
