# Формы проекта

from django import forms
from .models import Topic, Entry # Импорт моделей для создания форм на их основе

class TopicForm(forms.ModelForm):
    class Meta: 
        # Указание на модель, на которой основана форма
        model = Topic
        # Какие поля будут в форме
        fields = ['text'] # Создание текстового поля в форме
        labels = {'text': ''} #  Указание не создавать подпись для текстового поля
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        # HTML-виджет с шириной текстового поля 80 символов
        widget = {'text': forms.Textarea(attrs={'cols': 80})}
