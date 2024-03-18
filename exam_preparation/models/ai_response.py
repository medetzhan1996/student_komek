from django.db import models
from django.contrib.auth import get_user_model

from exam_preparation.abstract.models.base import BaseModel
from exam_preparation.models.ai_request import AIRequest

User = get_user_model()


class AIResponse(BaseModel):
    """
    Запрос к ИИ
    """
    text = models.TextField()
    ai_request = models.ForeignKey(
        AIRequest, on_delete=models.CASCADE,
        related_name='ai_responses',
        verbose_name="ИИ запрос"
    )

    def __str__(self):
        return "Запрос: {}, Результат: {}".format(
            self.ai_request.text, self.text
        )

    class Meta:
        indexes = [
            models.Index(fields=['text']),
        ]



