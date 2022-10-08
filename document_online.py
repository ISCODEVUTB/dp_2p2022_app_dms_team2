from abc import abstractmethod, ABC
from IOnline import IOnline
from document import Document


class DocumentOnline(ABC, Document, IOnline):

    def __init__(self, year=0, authors=[], edition="", publisher="", formats=[], idioms=[], pages=0, title="") -> None:
        super().__init__(year, authors, edition, publisher, formats, idioms, pages, title)

    @abstractmethod
    def publish(self):
        pass
    
    @abstractmethod
    def discontinue(self):
        pass

    @abstractmethod
    def versioning(self):
        pass

    def embebed(self, web):
        return f"Se embebio el documento en la web {web}"
    
    def open_in_browser(self):
        return "Abriendo documento..."


    def __str__(self):
        return {f'year: {self.year}, authors: {self.authors}, edition:{self.edition}, publisher:{self.publisher}, formats: {self.formats}, idioms:{self.idioms}, pages:{self.pages}, title:{self.title}'}
