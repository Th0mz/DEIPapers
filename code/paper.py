from re import A


class Paper:
    def __init__(self, title, authors, abstract, logoUrl, docUrl, id=0):
        self.id = id
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.logoUrl = logoUrl
        self.docUrl = docUrl

    def __str__(self) -> str:
        return "{ " + f"\"id\": {str(self.id)}, \"title\": \"{self.title}\", \"authors\": \"{self.authors}\", \"abstract\": \"{self.abstract}\", \"logoUrl\": \"{self.logoUrl}\", \"docUrl\": \"{self.docUrl}\"" + " }"