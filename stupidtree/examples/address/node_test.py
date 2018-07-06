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

from stupidtree.examples.address.level import Level
from .node import AddressNode


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
        self.assertEqual(n3.path_value(), n7.path_value())
        self.assertEqual(n3.csv_path_value(), n7.csv_path_value())
        n8 = AddressNode(data=None, level=None, parent=None)
        n9 = AddressNode(data=None, level=None, parent=None)
        self.assertEqual(n8, n9)
        self.assertEqual(n8.path_value(), n9.path_value())
        self.assertEqual(n8.csv_path_value(), n9.csv_path_value())


if __name__ == "__main__":
    unittest.main()
