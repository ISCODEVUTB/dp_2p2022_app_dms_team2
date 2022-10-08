from abc import abstractmethod, ABC
from IPdf import IPdf
from document import Document

class DocumentPdf(ABC, Document, IPdf):

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

    def sign(self, sign: str):
        return f"Firmamos el pdf digitalment con la firma {sign}"
    
    def compress(self, compress_quality: str):
        return f"se comprimio el pdf a calidad {compress_quality}"
    
    def add_watermark(self, mark: str):
        return f"Se coloco la marca de agua {mark} al pdf"


    def __str__(self):
        return {f'year: {self.year}, authors: {self.authors}, edition:{self.edition}, publisher:{self.publisher}, formats: {self.formats}, idioms:{self.idioms}, pages:{self.pages}, title:{self.title}'}
