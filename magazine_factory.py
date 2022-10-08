from abstract_factory import AbstractFactory
from magazine_online import MagazineOnline
from magazine_pdf import MagazinePdf
from document_online import DocumentOnline
from document_pdf import DocumentPdf

class MagazineFactory(AbstractFactory):

    def get_online(self) -> DocumentOnline:
        return MagazineOnline()

    def get_pdf(self) -> DocumentPdf:
        return MagazinePdf()