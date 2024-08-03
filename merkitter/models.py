from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_profile_pic = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self) -> str:
        return f'{self.user.first_name}-{self.user.pk}'


class Chat(models.Model):
    users = models.ManyToManyField(User, related_name='users', verbose_name='Пользователи')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self) -> str:
        return str(self.pk)


class Message(models.Model):
    content = models.TextField(verbose_name='Содержимое сообщения')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Сообщение')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Отправитель')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self) -> str:
        return str(self.chat.pk)
