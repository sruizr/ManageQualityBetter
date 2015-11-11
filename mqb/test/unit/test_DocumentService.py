import unittest
from mqb.app.documentservice import PdfGenerator, MailGenerator
import os
import mqb.test.unit.test_helper as th
import pdb


class TestMailGenerator(unittest.TestCase):

    def setUp(self):
        self.mail_generator = MailGenerator(
                                            th.get_template_path())
        self.variables = {
            "fromSource": "me@me.com",
            "toDestination": "toTest@test.com",
            "ccDestination": "ccTest@test.com",
            "subjectMessage": "Hello world",
            "bodyMessage": "Hey world",
            "filePath": os.path.join(th.get_template_path(),
                                     "img", "smile.png")
        }

    def test_mail_is_properly_parsed(self):

        xml_mail = self.mail_generator.parse_mail("hello.mail", self.variables)

        assert(xml_mail)
        self.assertNotEquals(xml_mail.find(self.variables["fromSource"]), -1)
        self.assertNotEquals(xml_mail.find(self.variables["toDestination"]),
                             -1)
        self.assertNotEquals(xml_mail.find(self.variables["subjectMessage"]),
                             -1)
        self.assertNotEquals(xml_mail.find(self.variables["ccDestination"]),
                             -1)
        self.assertNotEquals(xml_mail.find(self.variables["bodyMessage"]), -1)
        self.assertNotEquals(xml_mail.find(self.variables["filePath"]), -1)

    def test_mail_structure(self):

        xml_mail = self.mail_generator.parse_mail("hello.mail", self.variables)
        mail = self.mail_generator.get_mail(xml_mail)

        # pdb.set_trace()
        self.assertEquals(mail["Subject"], "Information:" +
                          self.variables["subjectMessage"])
        self.assertEquals(mail["To"], self.variables["toDestination"])
        self.assertEquals(mail["CC"], self.variables["ccDestination"])



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
