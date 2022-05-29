from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Тема, изучаемая пользователем."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Представление темы в виде её названия."""
        return self.text

class Entry(models.Model):
    """Запись по теме."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # установка зависимости от модели Topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Представление записи в виде текстого превью не более 50 символов."""
        if len(self.text) < 50:
            return self.text
        else:
            return f'{self.text[:50]}...'