from django.shortcuts import render
from django.http import HttpResponse
 

# Create your views here.
def displayPapers (request):
    return render(request, 'papers/papersList.html', {'value' : 10})
