from django.shortcuts import render, HttpResponse
from .models import project
from .forms import Mensajeform
from .intents import intents
import json
# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np

import tensorflow as tf
import random
import tflearn

# Create your views here.
def home(request):
    mensaje_form = Mensajeform()
    mensajes = project.objects.all() 
    if request.method == 'POST':
        data=request.POST['mensaje']
        #print(data)
        p = project(mensaje=data)
        p.save()
        responses=response(data)
        if responses:
            p = project(nombre='taker',mensaje=responses)
            p.save()
    return render(request, "core/home.html", {'form':mensaje_form,'mensajes':mensajes})


#**********************************+
#with open('/prueba4.json', 'r') as f:
 #   intents = json.load(f)
