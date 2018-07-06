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
from stupidtree.examples.address.pcd_tree import PCDTree


class TestPCDTree(unittest.TestCase):

    def test_put(self):
        tree = PCDTree()
        a0 = '浙江省 杭州市 西湖区'
        tree.put(a0)
        self.assertEqual(4, tree.size())
        tree.print()
        a1 = '浙江省 杭州市 江干区'
        tree.put(a1)
        self.assertEqual(5, tree.size())

        nodes = tree.get('浙江省')
        self.assertEqual(1, len(nodes))
        for n in nodes:
            self.assertEqual(Level.PROVINCE, n.tag)

    def test_remove(self):
        tree = PCDTree()
        a0 = '浙江省 杭州市 西湖区'
        tree.put(a0)
        a1 = '浙江省 杭州市 江干区'
        tree.put(a1)
        tree.print()

        tree.remove('江干区')
        self.assertEqual(4, tree.size())
        tree.print()

        tree.remove('浙江省')
        self.assertEqual(1, tree.size())
        tree.print()

        tree.remove('')
        print()
        tree.print()
        self.assertEqual(0, tree.size())


if __name__ == "__main__":
    unittest.main()
