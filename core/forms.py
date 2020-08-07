from django import forms
from .models import project

class Mensajeform(forms.Form):

    mensaje = forms.CharField(label="msj",required=True, help_text="Type message..", widget=forms.Textarea)
        