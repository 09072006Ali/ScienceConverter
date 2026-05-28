import unittest
from app import celsius_to_fahrenheit

class TestConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        # Doğrulama: 20 derece 68 Fahrenhayt olmalıdır
        self.assertEqual(celsius_to_fahrenheit(20), 68.0)
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

if __name__ == '__main__':
    unittest.main()