from django.contrib.auth.models import User
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from hashlib import md5

# класс ссылки,в котором записаны:
# имя полной ссылки
# имя объекта
# автор объекта
# хэш, для создания короткой ссылки
class URL(models.Model):
    full_url = models.URLField(verbose_name='Имя ссылки')
    short_name = models.CharField(max_length=50, verbose_name='Краткое имя', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    url_hash = models.URLField(verbose_name='Хэш', unique=True)

    def __str__(self):
        return self.full_url

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        val = URLValidator()
        try:
            val(self.full_url)
        except ValidationError as e:
            raise e

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
