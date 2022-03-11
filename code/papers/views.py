from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apiCalls import error_messages, postPaper
from apiCalls import getPapers, getPaper, deletePaper, postPaper, putPaper

from papers.forms import PaperForm
from paper import Paper
from urllib.parse import unquote

# Create your views here.
def displayPapers (request):
    papers = getPapers(limit=100)
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

    return render(request, 'papers/error.html', {'error' : error, 'message' : message})

@csrf_exempt
def newPaper (request):
    if request.method == 'POST':
        
        paperVariables = unquote(request.body).split('&')
        paperInfo = {
            'title' : '',
            'authors' : '',
            'abstract' : '',
            'docUrl' : '',
            'logoUrl' : ''
        }
        for variable in paperVariables:
            variable = variable.split('=')
            paperInfo[variable[0]] = variable[1]
        
        paper = Paper(paperInfo['title'], paperInfo['authors'], paperInfo['abstract'], paperInfo['logoUrl'], paperInfo['docUrl'])
        status = postPaper(paper)

        # No error detected
        error = False
        message = "Paper added with success"

        # Error detected
        if status >= 400:
            error = True
            message =  error_messages[status]

        return render(request, 'papers/error.html', {'error' : error, 'message' : message})
    elif request.method == 'GET':
        form = PaperForm()
        return render(request, 'papers/newPaperForm.html', {'form' : form})
        
        
    

@csrf_exempt
def editPaper(request, paperID):

    print(request.method)

    if request.method == 'POST':

        paperVariables = unquote(request.body).split('&')
        paperInfo = {
            'title' : '',
            'authors' : '',
            'abstract' : '',
            'docUrl' : '',
            'logoUrl' : ''
        }
        for variable in paperVariables:
            variable = variable.split('=')
            paperInfo[variable[0]] = variable[1]
        
        paper = Paper(paperInfo['title'], paperInfo['authors'], paperInfo['abstract'], paperInfo['logoUrl'], paperInfo['docUrl'])
        status = putPaper(paperID, paper)

        # No error detected
        error = False
        message = "Paper edited with success"

        # Error detected
        if status >= 400:
            error = True
            message =  error_messages[status]

        return render(request, 'papers/error.html', {'error' : error, 'message' : message})
    elif request.method == 'GET':
        form = PaperForm()
        return render(request, 'papers/editPaper.html', {'form' : form, 'paperID' : paperID})
