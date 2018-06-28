import unittest
from .node import AddressNode
from stupidtree.address.level import Level


class TestNode(unittest.TestCase):

    def test_equality(self):
        n0 = AddressNode(data='中国', level=Level.COUNTRY, parent=None)
        n1 = AddressNode(data='浙江', level=Level.PROVINCE, parent=n0)
        n2 = AddressNode(data='浙江', level=Level.CITY, parent=n0)
        n3 = AddressNode(data='浙江', level=Level.PROVINCE, parent=None)
        n4 = AddressNode(data='杭州', level=Level.PROVINCE, parent=n0)
        n5 = AddressNode(data='杭州', level=Level.CITY, parent=n0)
        n6 = AddressNode(data='杭州', level=Level.CITY, parent=n1)
        self.assertNotEqual(n0, n1)
        self.assertNotEqual(n1, n2)
        self.assertNotEqual(n2, n3)
        self.assertNotEqual(n3, n4)
        self.assertNotEqual(n4, n5)
        self.assertNotEqual(n5, n6)
        n7 = AddressNode(data='浙江', level=Level.PROVINCE, parent=None)
        self.assertEqual(n3, n7)
        self.assertEqual(n3.address(), n7.address())
        self.assertEqual(n3.csv_address(), n7.csv_address())
        n8 = AddressNode(data=None, level=None, parent=None)
        n9 = AddressNode(data=None, level=None, parent=None)
        self.assertEqual(n8, n9)
        self.assertEqual(n8.address(), n9.address())
        self.assertEqual(n8.csv_address(), n9.csv_address())


if __name__ == "__main__":
    unittest.main()
