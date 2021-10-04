import unittest
import os

from .context import pdf
from sizer.__main__ import images


class TestPdf(unittest.TestCase):
    def setUp(self):
        self.pdf = pdf.Pdf(images)


class TestWriteReport(TestPdf):
    def test_write_report(self):
        self.pdf.write_report()
        self.assertTrue(os.path.isfile(self.pdf.out))
        os.remove(self.pdf.out)


if __name__ == '__main__':
    unittest.main()
