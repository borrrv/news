from django.db import models
from users.models import Users


class BaseModel(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now=True,
    )

    class Meta:
        abstract = True


class News(BaseModel):
    title = models.CharField(
        "Название новости",
        max_length=100,
    )
    author = models.ForeignKey(
        Users,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        related_name="news",
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"{self.author}, {self.title}"


class Comments(BaseModel):
    author = models.ForeignKey(
        Users,
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )
    news = models.ForeignKey(
        News,
        verbose_name="Новость",
        on_delete=models.CASCADE,
        related_name="comments",
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.author}, {self.news}"
