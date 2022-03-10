from ctypes import util
from django.shortcuts import render

from apiCalls import getPapers
 

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

    print(papers)
    return render(request, 'papers/papersList.html', {'papers' : papers})
