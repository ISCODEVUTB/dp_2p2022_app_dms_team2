from enumerations import Format

class Document:
    _year: int
    _authors: list[str]
    _edition: str
    _publisher: str
    _formats: list[Format]
    _idioms: list[str]
    _pages: int
    _title: str

    def __init__(self, year=0, authors=[], edition="", publisher="", formats=[], idioms=[], pages=0, title="") -> None:
        self._year = year
        self._authors = authors
        self._edition = edition
        self._publisher = publisher
        self._formats = formats
        self._idioms = idioms
        self._title = title
        self._pages = pages

    @property
    def year(self) -> str:
        return self._year

    @year.setter
    def year(self, year: str) -> None:
        self._year = year

    @property
    def authors(self) -> list[str]:
        return self._authors

    @authors.setter
    def authors(self, author: str) -> None:
        self._authors.append(author)

    @property
    def edition(self) -> str:
        return self._edition

    @edition.setter
    def edition(self, edition: str) -> None:
        self._edition = edition

    @property
    def publisher(self) -> str:
        return self._publisher

    @publisher.setter
    def publisher(self, publisher: str) -> None:
        self._publisher = publisher

    @property
    def formats(self) -> list[Format]:
        return self._formats

    @formats.setter
    def formats(self, format: Format) -> None:
        self._formats.append(format)

    @property
    def idioms(self) -> list[str]:
        return self._idioms

    @idioms.setter
    def idioms(self, idiom: str) -> None:
        self._idioms.append(idiom)

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, isbn: str) -> None:
        self._isbn = isbn

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        self._pages = pages