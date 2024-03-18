from django.db import models
from django.contrib.auth import get_user_model

from exam_preparation.abstract.models.base import BaseModel

User = get_user_model()


class AIRequest(BaseModel):
    """
    Запрос к ИИ
    """
    text = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='ai_requests',
        verbose_name="Автор"
    )

    def __str__(self):
        return "Автор: {}, Запрос: {}".format(
            self.user, self.text
        )

    class Meta:
        indexes = [
            models.Index(fields=['text']),
        ]



