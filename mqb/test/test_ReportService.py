import unittest
import mqb.app.services


class TestReportService(unittest.TestCase):

    def test_latex_parser_generates_pdf(self):
        self.service = mqb.app.services.ReportingService()
        pass

if __name__ == '__main__':
    unittest.main()
