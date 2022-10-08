from document_online import DocumentOnline
from document_pdf import DocumentPdf


class ScientistPdf(DocumentPdf):
    _doi: str

    def __init__(self, year=0, authors=[], edition="", publisher="", formats=[], idioms=[], pages=0, title="", doi = "") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)
        self._doi = doi

    def publish():
        return "Publicando MagazinePdf"
    
    def discontinue():
        return "MagazinePdf a sido descontinuado"

    def versioning():
        return "Se ha creado nueva version de MagazinePdf"