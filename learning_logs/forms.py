from django import forms
#Any page that lets a user enter/submit information on a web page is a form.
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''} #Tells Django not a generate a label for the text field.

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        #A widget is a HTML form element.
        #Overriding the default to ensure users have enough room for an entry.
