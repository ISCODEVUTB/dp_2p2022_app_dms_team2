from document_online import DocumentOnline


class MagazineOnline(DocumentOnline):
    _issn: str

    def __init__(self, year=0, authors=[], edition="", publisher="", formats=[], idioms=[], pages=0, title="", issn="") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)
        self._issn = issn

    def publish():
        return "Publicando MagazineOnline"
    
    def discontinue():
        return "MagazineOnline a sido descontinuado"

    def versioning():
        return "Se ha creado nueva version de MagazineOnline"