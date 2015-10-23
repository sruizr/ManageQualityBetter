import unittest
from mqb.app.reportsservices import ReportGenerator
import os


class TestReportGenerator(unittest.TestCase):

    templates_path = os.getcwd()
    templates_path = os.path.join(templates_path, "mqb",
                                  "test", "templates")

    def test_generate_something(self):
        template = 'hello.tex'
        var = {}
        report_generator = ReportGenerator(TestReportGenerator.templates_path)
        pdf = report_generator.printToPDF(template, var)
        assert pdf

    def test_variables_are_replaced(self):
            pass

if __name__ == '__main__':
    unittest.main()
