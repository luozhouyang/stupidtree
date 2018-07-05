import unittest
from .level import Level


class TestLevel(unittest.TestCase):

    def test_level(self):
        l0 = Level.COUNTRY
        self.assertEqual(1, l0)
        l1 = Level.PROVINCE
        self.assertNotEqual(l0, l1)
        self.assertEqual(2, l1)
        l2 = Level.CITY
        self.assertEqual(3, l2)
        self.assertNotEqual(l0, l2)
        self.assertNotEqual(l1, l2)
        l3 = Level.DISTRICT
        self.assertEqual(4, l3)
        self.assertNotEqual(l0, l3)
        self.assertNotEqual(l1, l3)
        self.assertNotEqual(l2, l3)
        l4 = Level.ROAD
        self.assertEqual(5, l4)
        self.assertNotEqual(l0, l4)
        self.assertNotEqual(l1, l4)
        self.assertNotEqual(l2, l4)
        self.assertNotEqual(l3, l4)


if __name__ == "__main__":
    unittest.main()
