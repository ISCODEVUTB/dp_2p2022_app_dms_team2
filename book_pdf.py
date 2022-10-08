from document_pdf import DocumentPdf


class BookPdf(DocumentPdf):
    _isbn: str
    
    def __init__(self, year=0, authors=..., edition="", publisher="", formats=..., idioms=..., pages=0, title="", isbn = "") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)
        self._isbn = isbn

    
    def publish(self):
        return "Publicando BookPdf"
    
    def discontinue(self):
        return "BookPdf a sido descontinuado"

    def versioning(self):
        return "Se ha creado nueva version de BookPdf"