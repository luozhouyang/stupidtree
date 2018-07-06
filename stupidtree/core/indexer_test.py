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

from .indexer import NodeDictIndexer
from .node import Node


class TestNodeDictIndexer(unittest.TestCase):

    def test_node_dict_indexer(self):
        n0 = Node(data='A', tag='TAG_0', parent=None)
        n1 = Node(data='B', tag='TAG_1', parent=None)
        n2 = Node(data='A', tag='TAG_0', parent=None)
        indexer = NodeDictIndexer()
        indexer.put(n0.data, n0)
        indexer.put(n1.data, n1)
        indexer.put(n2.data, n2)

        self.assertEqual(1, len(indexer.get(n0.data)))
        self.assertEqual(1, len(indexer.get(n1.data)))

        indexer.remove(n0)
        for n in indexer.get(n0.data):
            print(n.data)
        self.assertEqual(0, len(indexer.get(n0.data)))
        self.assertEqual(1, len(indexer.get(n1.data)))

        indexer.remove(n1)
        self.assertEqual(0, len(indexer.get(n1.data)))


if __name__ == "__main__":
    unittest.main()
