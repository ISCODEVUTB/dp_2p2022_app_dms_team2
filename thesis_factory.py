from abstract_factory import AbstractFactory
from thesis_online import ThesisOnline
from thesis_pdf import ThesisPdf
from document_online import DocumentOnline
from document_pdf import DocumentPdf

class ThesisFactory(AbstractFactory):

    def get_online(self) -> DocumentOnline:
        return ThesisOnline()

    def get_pdf(self) -> DocumentPdf:
        return ThesisPdf()