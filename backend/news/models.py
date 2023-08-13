from django.db import models

from users.models import Users


class BaseModel(models.Model):
    """Базовая модель с текстом и датой публикации"""
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now=True,
    )

    class Meta:
        abstract = True


class News(BaseModel):
    """Модель новостей"""
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
    likes = models.ManyToManyField(
        Users,
        default=0,
        verbose_name="Лайки",
        related_name='likes',
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"{self.author}, {self.title}"


class Comments(BaseModel):
    """Модель комментариев"""
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
