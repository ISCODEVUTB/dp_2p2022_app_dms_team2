import unittest
from book_pdf import BookPdf
from book_online import BookOnline
from enumerations import Format

class TestNewLigue(unittest.TestCase):

    book_pdf = BookPdf(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", isbn = "93423529923", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])
    book_online = BookOnline(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", isbn = "93423529923", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])

    def test_book_online_publish(self):
        result = self.book_online.publish()
        self.assertEqual(result, "Publicando BookOnline")

    def test_book_online_discontinue(self):
        result = self.book_online.discontinue()
        self.assertEqual(result, "BookOnline a sido descontinuado")

    def test_book_online_versioning(self):
        result = self.book_online.versioning()
        self.assertEqual(result, "Se ha creado nueva version de BookOnline")

    def test_book_pdf_publish(self):
        result = self.book_pdf.publish()
        self.assertEqual(result, "Publicando BookPdf")

    def test_book_pdf_discontinue(self):
        result = self.book_pdf.discontinue()
        self.assertEqual(result, "BookPdf a sido descontinuado")

    def test_book_pdf_versioning(self):
        result = self.book_pdf.versioning()
        self.assertEqual(result, "Se ha creado nueva version de BookPdf")


if __name__ == '__main__':
    unittest.main()