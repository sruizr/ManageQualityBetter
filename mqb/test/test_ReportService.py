import unittest
from mqb.app.reportsservices import ReportGenerator
import os


class TestReportGenerator(unittest.TestCase):

    templates_path = os.getcwd()
    templates_path = os.path.join(templates_path, "mqb",
                                  "test", "templates")
    pdf_directory = os.path.join(templates_path, "pdfOutput")

    def test_texfile_is_parsed(self):
        template = "helloVariable.tex"
        name = "Salvador"
        var = {"name": name}

        report_generator = ReportGenerator(TestReportGenerator.templates_path,
                                           TestReportGenerator.pdf_directory)
        tex_document = report_generator.parse_tex_file(template, var)
        self.assertTrue(tex_document.find(name))

    def test_generate_something(self):
        template = 'hello.tex'
        var = {}
        report_generator = ReportGenerator(TestReportGenerator.templates_path,
                                           TestReportGenerator.pdf_directory)
        tex_document = report_generator.parse_tex_file(template, var)
        pdf = report_generator.print_to_PDF(tex_document)

        assert pdf

    def test_generate_pdf_with_images(self):
        pass


if __name__ == '__main__':
    unittest.main()
