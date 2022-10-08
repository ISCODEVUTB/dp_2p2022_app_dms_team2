from document_online import DocumentOnline


class ThesisOnline(DocumentOnline):
    _university: str

    def __init__(self, year=0, authors=[], edition="", publisher="", formats=[], idioms=[], pages=0, title="", university = "") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)
        self._university = university

    def publish(self):
        return "Publicando ThesisOnline"
    
    def discontinue(self):
        return "ThesisOnline a sido descontinuado"

    def versioning(self):
        return "Se ha creado nueva version de ThesisOnline"