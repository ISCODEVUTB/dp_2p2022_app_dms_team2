import unittest
from book_pdf import BookPdf
from book_online import BookOnline
from magazine_pdf import MagazinePdf
from magazine_online import MagazineOnline
from thesis_pdf import ThesisPdf
from thesis_online import ThesisOnline
from scientist_pdf import ScientistPdf
from scientist_online import ScientistOnline
from enumerations import Format

class TestDms(unittest.TestCase):

    book_pdf = BookPdf(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", isbn = "93423529923", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])
    book_online = BookOnline(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", isbn = "93423529923", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])

    magazine_pdf = MagazinePdf(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", issn= "93423529923", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])
    magazine_online = MagazineOnline(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", issn= "93423529923", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])

    
    thesis_pdf = ThesisPdf(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", university= "Universidad Tecnologica de Bolivar", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])
    thesis_online = ThesisOnline(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", university= "Universidad Tecnologica de Bolivar", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])

    
    scientist_pdf = ScientistPdf(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", doi= "93423529923", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])
    scientist_online = ScientistOnline(year=2022, authors=["Erick", "Maria"],edition="2",publisher="Editorial UTB", doi= "93423529923", formats=[Format.DIGITAL], pages=340, title="My example", idioms=["es", "en"])

    def test_book_online_publish(self):
        result = self.book_online.publish()
        self.assertEqual(result, "Publicando BookOnline")

    def test_book_online_discontinue(self):
        result = self.book_online.discontinue()
        self.assertEqual(result, "BookOnline a sido descontinuado")

    def test_book_online_versioning(self):
        result = self.book_online.versioning()
        self.assertEqual(result, "Se ha creado nueva version de BookOnline")

    def test_book_pdf_sign(self):
        result = self.book_pdf.sign("2345783")
        self.assertEqual(result, "Firmamos el pdf digitalment con la firma 2345783")

    def test_book_pdf_watermark(self):
        result = self.book_pdf.add_watermark("example")
        self.assertEqual(result, "Se coloco la marca de agua example al pdf")

    def test_book_pdf_compress(self):
        result = self.book_pdf.compress("medium")
        self.assertEqual(result, "se comprimio el pdf a calidad medium")

    def test_book_pdf_publish(self):
        result = self.book_pdf.publish()
        self.assertEqual(result, "Publicando BookPdf")

    def test_book_pdf_discontinue(self):
        result = self.book_pdf.discontinue()
        self.assertEqual(result, "BookPdf a sido descontinuado")

    def test_book_pdf_versioning(self):
        result = self.book_pdf.versioning()
        self.assertEqual(result, "Se ha creado nueva version de BookPdf")


    def test_magazine_online_publish(self):
        result = self.magazine_online.publish()
        self.assertEqual(result, "Publicando MagazineOnline")

    def test_magazine_online_discontinue(self):
        result = self.magazine_online.discontinue()
        self.assertEqual(result, "MagazineOnline a sido descontinuado")

    def test_magazine_online_versioning(self):
        result = self.magazine_online.versioning()
        self.assertEqual(result, "Se ha creado nueva version de MagazineOnline")

    def test_magazine_online_embebed(self):
        result = self.magazine_online.embebed("example.com")
        self.assertEqual(result, "Se embebio el documento en la web example.com")

    def test_magazine_online_browser(self):
        result = self.magazine_online.open_in_browser()
        self.assertEqual(result, "Abriendo documento...")

    def test_magazine_pdf_publish(self):
        result = self.magazine_pdf.publish()
        self.assertEqual(result, "Publicando MagazinePdf")

    def test_magazine_pdf_discontinue(self):
        result = self.magazine_pdf.discontinue()
        self.assertEqual(result, "MagazinePdf a sido descontinuado")

    def test_magazine_pdf_versioning(self):
        result = self.magazine_pdf.versioning()
        self.assertEqual(result, "Se ha creado nueva version de MagazinePdf")


    def test_thesis_online_publish(self):
        result = self.thesis_online.publish()
        self.assertEqual(result, "Publicando ThesisOnline")

    def test_thesis_online_discontinue(self):
        result = self.thesis_online.discontinue()
        self.assertEqual(result, "ThesisOnline a sido descontinuado")

    def test_thesis_online_versioning(self):
        result = self.thesis_online.versioning()
        self.assertEqual(result, "Se ha creado nueva version de ThesisOnline")

    def test_thesis_pdf_publish(self):
        result = self.thesis_pdf.publish()
        self.assertEqual(result, "Publicando ThesisPdf")

    def test_thesis_pdf_discontinue(self):
        result = self.thesis_pdf.discontinue()
        self.assertEqual(result, "ThesisPdf a sido descontinuado")

    def test_thesis_pdf_versioning(self):
        result = self.thesis_pdf.versioning()
        self.assertEqual(result, "Se ha creado nueva version de ThesisPdf")


    def test_scientist_online_publish(self):
        result = self.scientist_online.publish()
        self.assertEqual(result, "Publicando ScientistOnline")

    def test_scientist_online_discontinue(self):
        result = self.scientist_online.discontinue()
        self.assertEqual(result, "ScientistOnline a sido descontinuado")

    def test_scientist_online_versioning(self):
        result = self.scientist_online.versioning()
        self.assertEqual(result, "Se ha creado nueva version de ScientistOnline")

    def test_scientist_pdf_publish(self):
        result = self.scientist_pdf.publish()
        self.assertEqual(result, "Publicando ScientistPdf")

    def test_scientist_pdf_discontinue(self):
        result = self.scientist_pdf.discontinue()
        self.assertEqual(result, "ScientistPdf a sido descontinuado")

    def test_scientist_pdf_versioning(self):
        result = self.scientist_pdf.versioning()
        self.assertEqual(result, "Se ha creado nueva version de ScientistPdf")


if __name__ == '__main__':
    unittest.main()