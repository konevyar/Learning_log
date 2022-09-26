# Project forms

from django import forms
from .models import Topic, Entry  # Importing models as base for forms creation


class TopicForm(forms.ModelForm):
    class Meta: 
        # Pointing at model, on which form is based
        model = Topic
        # Fields in new form:
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        # HTML-widget with a text field width of 80 characters
        widget = {'text': forms.Textarea(attrs={'cols': 80})}
