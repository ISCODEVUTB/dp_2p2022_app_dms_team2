from document_online import DocumentOnline


class ScientistOnline(DocumentOnline):
    _doi: str

    def __init__(self, year=0, authors=[], edition="", publisher="", formats=[], idioms=[], pages=0, title="", doi = "") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)
        self._doi = doi

    def publish():
        return "Publicando ScientistOnline"
    
    def discontinue():
        return "ScientistOnline a sido descontinuado"

    def versioning():
        return "Se ha creado nueva version de ScientistOnline"