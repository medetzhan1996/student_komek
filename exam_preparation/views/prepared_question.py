from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import PreparedQuestion
from exam_preparation.forms.prepared_question import PreparedQuestionForm


class PreparedQuestionMixin(LoginRequiredMixin):
    model = PreparedQuestion
    success_url = reverse_lazy('exam_preparation:prepared-question-list')
    context_object_name = 'prepared_questions'


class PreparedQuestionEditMixin(PreparedQuestionMixin):
    form_class = PreparedQuestionForm


class PreparedQuestionListView(PreparedQuestionMixin, ListView):
    template_name = 'exam_preparation/prepared_question/list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter_by_user(user_id=user.id)
        return queryset


class PreparedQuestionCreateView(PreparedQuestionEditMixin, CreateView):
    template_name = 'exam_preparation/prepared_question/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PreparedQuestionUpdateView(PreparedQuestionEditMixin, UpdateView):
    template_name = 'exam_preparation/prepared_question/form.html'


class PreparedQuestionDetailView(PreparedQuestionMixin, DetailView):
    template_name = 'exam_preparation/prepared_question/detail.html'


class PreparedQuestionDeleteView(PreparedQuestionMixin, DeleteView):
    template_name = 'exam_preparation/prepared_question/delete.html'






