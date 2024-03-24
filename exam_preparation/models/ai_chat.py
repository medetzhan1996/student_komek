from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet

from exam_preparation.abstract.models.base import BaseModel

User = get_user_model()


class AIChatQueryset(QuerySet):

    def filter_by_user(self, user_id: int):
        return self.filter(user_id=user_id)


class AIChat(BaseModel):
    """
    Запрос к ИИ
    """
    request = models.TextField()
    response = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='ai_requests',
        verbose_name="Автор"
    )
    objects = AIChatQueryset.as_manager()

    def __str__(self):
        return "Автор: {}, Запрос: {}".format(
            self.user, self.request
        )

    class Meta:
        indexes = [
            models.Index(fields=['request', 'response']),
        ]



