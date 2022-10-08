from document_online import DocumentOnline
from document_pdf import DocumentPdf
from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def get_online(self) -> DocumentOnline:
        pass

    @abstractmethod
    def get_pdf(self) -> DocumentPdf:
        pass