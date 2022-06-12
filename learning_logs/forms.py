# Project forms

from django import forms
from .models import Topic, Entry # Importing models as base for forms creation

class TopicForm(forms.ModelForm):
    class Meta: 
        # Pointing at model, on which form is based
        model = Topic
        # Fiels in new form:
        fields = ['text'] # Text field
        labels = {'text': ''} #  Insctruction not to create signature for text field
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        # HTML-widget with a text field width of 80 characters
        widget = {'text': forms.Textarea(attrs={'cols': 80})}
