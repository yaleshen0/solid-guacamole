import unittest
from main import is_bulky, is_heavy, sort
class TestPackageSorting(unittest.TestCase):
    # Tests for is_bulky()
    def test_is_bulky_volume_exceeds(self):
        self.assertTrue(is_bulky(100, 100, 100))  # 100*100*100 = 1,000,000 → bulky

    def test_is_bulky_dimension_exceeds(self):
        self.assertTrue(is_bulky(150, 10, 10))  # width=150 → bulky

    def test_is_bulky_not_bulky(self):
        self.assertFalse(is_bulky(50, 50, 50))  # 50*50*50=125,000 (<1M) and all dims <150 → not bulky

    # Tests for is_heavy()
    def test_is_heavy_true(self):
        self.assertTrue(is_heavy(20))  # mass=20 → heavy

    def test_is_heavy_false(self):
        self.assertFalse(is_heavy(19))  # mass=19 → not heavy

    # Tests for sort()
    def test_sort_rejected(self):
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")  # bulky + heavy → REJECTED

    def test_sort_special_bulky(self):
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")  # bulky only → SPECIAL

    def test_sort_special_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")  # heavy only → SPECIAL

    def test_sort_standard(self):
        self.assertEqual(sort(10, 10, 10, 10), "STANDARD")  # neither → STANDARD

if __name__ == "__main__":
    unittest.main()