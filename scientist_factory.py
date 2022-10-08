from abstract_factory import AbstractFactory
from scientist_online import ScientistOnline
from scientist_pdf import ScientistPdf
from document_online import DocumentOnline
from document_pdf import DocumentPdf

class ScientistFactory(AbstractFactory):

    def get_online(self) -> DocumentOnline:
        return ScientistOnline()

    def get_pdf(self) -> DocumentPdf:
        return ScientistPdf()