from document_pdf import DocumentPdf


class MagazinePdf(DocumentPdf):
    _issn: str

    def __init__(self, year=0, authors=[], edition="", publisher="", formats=[], idioms=[], pages=0, title="", issn="") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)
        self._issn = issn

    def publish(self):
        return "Publicando MagazinePdf"
    
    def discontinue(self):
        return "MagazinePdf a sido descontinuado"

    def versioning(self):
        return "Se ha creado nueva version de MagazinePdf"