import unittest

from .context import size


class TestGatherImages(unittest.TestCase):
    def test_gather_images(self):
        self.assertEqual(size.gather_images(size.PATH), 1, "Should be 1 for normal execution")


if __name__ == '__main__':
    unittest.main()
