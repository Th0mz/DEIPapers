from ctypes import util
from email import message
from django.shortcuts import render

from apiCalls import error_messages
from apiCalls import getPapers, getPaper, deletePaper

# Create your views here.
def displayPapers (request):
    allPaperInfo = getPapers()
    
    papers = []
    for paper in allPaperInfo:
        papers.append({
            'title' : paper['title'],
            'authors' : paper['authors'],
            'logoUrl' : paper['logoUrl'],
            'id' : paper['id']
        })

    return render(request, 'papers/papersList.html', {'papers' : papers})


def displayPaper (request, paperID):
    paper = getPaper(paperID)
    return render(request, 'papers/specificPaper.html', {'paper' : paper})


def removePaper(request, paperID):
    status = deletePaper(paperID)

    # No error detected
    error = False
    message = "Paper deleted with success"

    # Error detected
    if status >= 400:
        error = True
        message =  error_messages[status]

    return render(request, 'papers/deletePaper.html', {'error' : error, 'message' : message})