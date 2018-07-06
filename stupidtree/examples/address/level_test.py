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
