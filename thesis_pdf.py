from document_pdf import DocumentPdf


class ThesisPdf(DocumentPdf):
    _university: str

    def __init__(self, year=0, authors=[], edition="", publisher="", formats=[], idioms=[], pages=0, title="", university = "") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)
        self._university = university

    def publish():
        return "Publicando ThesisPdf"
    
    def discontinue():
        return "ThesisPdf a sido descontinuado"

    def versioning():
        return "Se ha creado nueva version de ThesisPdf"