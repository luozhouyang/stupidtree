# Copyright (c) 2018 luozhouyang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
