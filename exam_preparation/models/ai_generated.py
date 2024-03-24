from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet

from exam_preparation.abstract.models.base import BaseModel
from ..constant import KIND_CHOICES, CHAT

User = get_user_model()


class AIChatQueryset(QuerySet):

    def filter_by_user(self, user_id: int):
        return self.filter(user_id=user_id)


class AIGenerated(BaseModel):
    """
    Запрос к ИИ
    """

    request = models.TextField()
    response = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ai_requests',
        verbose_name="Автор"
    )
    kind = models.CharField(
        choices=KIND_CHOICES,
        max_length=320,
        default=CHAT
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



