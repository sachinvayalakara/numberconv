from django.shortcuts import render
import inflect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import pyttsx3
import os 

# Create your views here.
def register(request):
    try:
        x = 0
        number=0
        if request.method == 'POST':
            number = request.POST['number']
            p = inflect.engine()
            x = p.number_to_words(number)
            engine = pyttsx3.init()
            text = x
            engine.say(text) 
            engine.runAndWait()
        return render(request, 'register.html',{'x':x,'number':number})

    except Exception as e:
        print(e)
        return HttpResponse(e)    
