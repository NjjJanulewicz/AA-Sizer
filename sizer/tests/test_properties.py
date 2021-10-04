import unittest

from .context import properties

IMAGE = "25bttn.img"
PATH = "rc/25bttn.img"
TO_STRING = "Name: 25bttn.img\nFormat: RGBA\nColor key: No\n" \
            "Image size: 165x270\nFrame size: 165x90\nFrames: 3\n\n"


class TestProperties(unittest.TestCase):
    def setUp(self):
        self.properties = properties.Properties(PATH)


class TestInit(TestProperties):
    def test_init(self):
        self.assertEqual(self.properties.name, IMAGE)


class TestToString(TestProperties):
    def test_to_string(self):
        self.assertEqual(self.properties.to_string(), TO_STRING)


if __name__ == '__main__':
    unittest.main()
