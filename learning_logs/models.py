from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Topic being studied by the user."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Представление темы в виде её названия."""
        return self.text

class Entry(models.Model):
    """Entry on Topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # setup dependence from model Topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Presenting Entry as a text preview of up to 50 characters."""
        if len(self.text) < 50:
            return self.text
        else:
            return f'{self.text[:50]}...'