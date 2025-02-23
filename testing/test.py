import unittest

class SimpleTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)


    def test_Upper(self):
        self.assertEqual(
            "enki".upper(),
            "ENKI"
        )

if __name__ == "__main__":
    unittest.main()