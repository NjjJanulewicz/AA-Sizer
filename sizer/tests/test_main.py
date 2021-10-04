import unittest

from .context import __main__


class TestGatherImages(unittest.TestCase):
    def test_gather_images(self):
        self.assertEqual(__main__.gather_images(__main__.PATH), 1, "Should be 1 for normal execution")


class TestConvertImg(unittest.TestCase):
    def test_convert_img(self):
        self.assertEqual(__main__.gather_images(__main__.PATH), 1, "Should be 1 for normal execution")


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(__main__.gather_images(__main__.PATH), 1, "Should be 1 for normal execution")


if __name__ == '__main__':
    unittest.main()
