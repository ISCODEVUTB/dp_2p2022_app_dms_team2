from abstract_factory import AbstractFactory
from book_online import BookOnline
from book_pdf import BookPdf
from document_online import DocumentOnline
from document_pdf import DocumentPdf

class BookFactory(AbstractFactory):

    def get_online(self) -> DocumentOnline:
        return BookOnline()

    def get_pdf(self) -> DocumentPdf:
        return BookPdf()