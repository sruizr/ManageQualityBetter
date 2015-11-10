import unittest
from mqb.app.documentservice import PdfGenerator, MailGenerator
import os
import test_helper as th
import shutil
import pdb


class TestMailGenerator(unittest.TestCase):

    def setup(self):
        self.mail_generator = MailGenerator(
                                            th.get_template_path())

    def test_mail_is_properly_parsed(self):
        variables = {
            "toDestination": "toTest@test.com",
            "ccDestination": "ccTest@test.com",
            "subjectMessage": "Hello world",
            "bodyMessage": "HHeeeey world",
            "filePath":
        }
        self.mail_generator.parse_mail("hello.mail", variables)


    def test_mail_structure(self):
        self.fail("Not implemented")


class TestPdfGenerator(unittest.TestCase):
    templates_path = th.get_template_path()

    pdf_directory = os.path.join(templates_path, "pdfOutput")

    def test_texfile_is_parsed(self):
        template = "helloVariable.tex"
        name = "Salvador"
        var = {"name": name}

        report_generator = PdfGenerator(TestPdfGenerator.templates_path,
                                        TestPdfGenerator.pdf_directory)
        tex_document = report_generator.parse_tex_file(template, var)
        self.assertTrue(tex_document.find(name))

    def test_generate_something(self):
        template = 'hello.tex'
        var = {}
        report_generator = PdfGenerator(TestPdfGenerator.templates_path,
                                        TestPdfGenerator.pdf_directory)
        tex_document = report_generator.parse_tex_file(template, var)
        pdf = report_generator.print_to_PDF(tex_document)

        assert pdf

    def test_generate_pdf_with_images(self):
        template = 'helloWithImage.tex'
        name = "Salvador"
        var = {"name": name}
        report_generator = PdfGenerator(TestPdfGenerator.templates_path,
                                        TestPdfGenerator.pdf_directory)
        tex_document = report_generator.parse_tex_file(template, var)
        pdf = report_generator.print_to_PDF(tex_document)

        assert pdf

    def test_pdf_can_be_saved(self):
        template = 'helloWithImage.tex'
        name = "Salvador"
        var = {"name": name}

        report_generator = PdfGenerator(TestPdfGenerator.templates_path,
                                        TestPdfGenerator.pdf_directory)
        tex_document = report_generator.parse_tex_file(template, var)
        pdf = report_generator.print_to_PDF(tex_document)

        # pdb.set_trace()
        saved_file = open(TestPdfGenerator.templates_path +
                          "\\test.pdf",
                          "wb")
        saved_file.write(pdf.read())
        self.assertGreater(saved_file.tell(), 0)
        saved_file.close()
        os.unlink(saved_file.name)

if __name__ == '__main__':
    unittest.main()
