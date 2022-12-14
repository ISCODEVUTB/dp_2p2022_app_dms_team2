from document_online import DocumentOnline


class BookOnline(DocumentOnline):
    _isbn: str
    
    def __init__(self, year=0, authors=..., edition="", publisher="", formats=..., idioms=..., pages=0, title="", isbn = "") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)
        self._isbn = isbn

    def publish(self):
        return "Publicando BookOnline"
    
    def discontinue(self):
        return "BookOnline a sido descontinuado"

    def versioning(self):
        return "Se ha creado nueva version de BookOnline"