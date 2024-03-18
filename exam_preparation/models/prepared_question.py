from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet

from exam_preparation.abstract.models.base import BaseModel

User = get_user_model()


class PreparedQuestionQueryset(QuerySet):

    def filter_by_user(self, user_id: int):
        return self.filter(user_id=user_id)


class PreparedQuestion(BaseModel):
    """
    Подготовленные вопросы
    """
    title = models.CharField(max_length=380, verbose_name="Название")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='prepared_questions',
        verbose_name="Автор"
    )
    content = models.TextField()
    objects = PreparedQuestionQueryset.as_manager()

    def __str__(self):
        return "Автор: {}, Название: {}".format(
            self.user, self.title
        )

    class Meta:
        indexes = [
            models.Index(fields=['title']),
        ]





