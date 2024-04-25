from django.forms import ModelForm
from django import forms
from .models import *

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widges = {
            'body': forms.TextInput(attrs={'placeholder':'type your message here ...', 'class':'p-4 text-black', 'maxlength':'300', 'autofocus' : True}),
        }