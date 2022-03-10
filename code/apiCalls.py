from numpy import isin
import requests
from paper import Paper

# Error Codes
OK = 200
PAPER_CREATED = 201
NULL_RESPONSE = 204

INVALID_INFO = 400
INVALID_TOKEN = 401
NO_PERMITION = 403
NOT_FOUND = 404

url = "https://aduck.rnl.tecnico.ulisboa.pt/istpaper/papers"
token = "ist195680"

def getPapers (offset=0, limit=10):
    """ Get <limit> papers beggining at <offset> from istPaper database """
    if (not isinstance(offset, int)) or (not isinstance(limit, int)):
        return INVALID_INFO

    headers = {
        "accept" : "application/json"
    }

    request = requests.get(url + f"?limit={limit}&offset={offset}", headers=headers)
    statusCode = request.status_code

    if statusCode == OK:
        papers = request.json()

        # ----- DEBUG ----- #
        #for paper in papers:
        #    print(f"ID : {paper['id']}    Nome : {paper['title']}")
        return papers

    return statusCode


def postPaper (paper):
    """ Create new entry on istPaper database """
    if not isinstance(paper, Paper):
        return INVALID_INFO

    headers = {
        "accept" : "application/json",
        "Authorization" : f"Bearer {token}",
        "Content-Type" : "application/json"
    }

    request = requests.post(url, headers=headers, data=str(paper))

    return request.status_code


def deletePaper (paperID):
    """ Delete an entry (with id = paperID) from istPaper database """
    if not isinstance(paperID, int):
        return INVALID_INFO

    headers = {
        "accept" : "*/*"
    }

    request = requests.delete(url + f"/{paperID}", headers=headers);

    return request.status_code


def getPaper (paperID : int):
    """ Get an entry (with id = paperID) from istPaper database """
    if not isinstance(paperID, int):
        return INVALID_INFO
    
    headers = {
        "accept" : "application/json"
    }

    request = requests.get(url + f"/{paperID}", headers=headers);
    statusCode = request.status_code

    if statusCode == OK:
        paper = request.json()
        
        # ----- DEBUG ----- #
        #print(paper)
        return paper

    return statusCode


def putPaper (paperID : int, paper : Paper):
    """ Update an entry (with id = paperID) on istPaper database """
    if (not isinstance(paper, Paper)) or (not isinstance(paperID, int)):
        return INVALID_INFO

    headers = {
        "accept" : "application/json",
        "Content-Type" : "application/json"
    }

    request = requests.put(url + f"/{paperID}", headers=headers, data=str(paper))

    return request.status_code