from abstract_factory import AbstractFactory
from book_factory import BookFactory
from magazine_factory import MagazineFactory
from thesis_factory import ThesisFactory
from scientist_factory import ScientistFactory


def read_document() -> AbstractFactory:
    factories = {
        "book": BookFactory(),
        "magazine": MagazineFactory(),
        "thesis": ThesisFactory(),
        "scientist": ScientistFactory()
    }

    while True:
        document_type = input("¿Que documento desea crear?: \n * book \n * magazine \n * thesis \n * scientist \n\n:")
        if document_type in factories:
            return factories[document_type]
        print(f"\nEl tipo de documento {document_type} no se encuentra entre las opciones validas.")


def main() -> None:
    factory = read_document()
    document_online = factory.get_online()
    document_pdf = factory.get_pdf()

    print(type(document_online))
    print(type(document_pdf))

if __name__ == '__main__':
    main()
