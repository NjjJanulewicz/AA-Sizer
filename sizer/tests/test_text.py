import unittest
import os

from .context import text
from sizer.__main__ import images


class TestText(unittest.TestCase):
    """
    thanks to Ryan Lundy -> how to tests file i/o

    What am I testing?
    That the file system works?
    That the files get saved to the right place?
    That you get the right set of files from a directory? Y
    But, I need to do something with the files I get.
    """
    def setUp(self):
        self.text = text.Text(images)


class TestWriteReport(TestText):
    def test_write_report(self):
        self.text.write_report()
        self.assertTrue(os.path.isfile(self.text.out))
        os.remove(self.text.out)


if __name__ == '__main__':
    unittest.main()
