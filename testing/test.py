import unittest

class SimpleTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)


    def test_Uper(self):
        self.assertEqual(
            "enki".upper(),
            "ENKI"
        )