import unittest
from .node import Node


class TestNode(unittest.TestCase):

    def test_equality(self):
        n0 = Node(data='', tag=None, parent=None)
        n1 = Node(data='A', tag=None, parent=None)
        n2 = Node(data='', tag='TAG_0', parent=None)
        n3 = Node(data='', tag=None, parent=n2)
        n4 = Node(data='', tag=None, parent=None)
        n5 = Node(data='', tag='TAG_1', parent=None)
        n6 = Node(data='', tag='TAG_0', parent=n4)

        self.assertEqual(n0, n4)
        self.assertNotEqual(n0, n1)
        self.assertNotEqual(n0, n2)
        self.assertNotEqual(n0, n3)
        self.assertNotEqual(n0, n5)
        self.assertNotEqual(n0, n6)
        self.assertNotEqual(n1, n2)
        self.assertNotEqual(n1, n3)
        self.assertNotEqual(n1, n4)
        self.assertNotEqual(n1, n5)
        self.assertNotEqual(n1, n6)
        self.assertNotEqual(n2, n3)
        self.assertNotEqual(n2, n4)
        self.assertNotEqual(n2, n5)
        self.assertNotEqual(n2, n6)
        self.assertNotEqual(n3, n4)
        self.assertNotEqual(n3, n5)
        self.assertNotEqual(n3, n6)
        self.assertNotEqual(n4, n5)
        self.assertNotEqual(n4, n6)
        self.assertNotEqual(n5, n6)


if __name__ == "__main__":
    unittest.main()
