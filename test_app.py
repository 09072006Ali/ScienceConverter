import unittest
from app import celsius_to_fahrenheit, km_to_miles
class TestConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        # Doğrulama: 20 derece 68 Fahrenhayt olmalıdır
        self.assertEqual(celsius_to_fahrenheit(20), 68.0)
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_km_to_miles(self):
        # Verification: 10 km should be approximately 6.21371 miles
        self.assertAlmostEqual(km_to_miles(10), 6.21371, places=5)

if __name__ == '__main__':
    unittest.main()