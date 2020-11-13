from django.shortcuts import render
import inflect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def register(request):
    try:
        if request.method == 'POST':
            number = request.POST['number']
            p = inflect.engine()
            x=p.number_to_words(number)
            print(x)

        return render(request, 'register.html',{'x':x})

    except Exception as e:
        print(e)
        return HttpResponse(e)    