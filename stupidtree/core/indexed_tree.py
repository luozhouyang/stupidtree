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

import abc

from .base_tree import BaseTree
from .indexer import NodeDictIndexer


class IndexedTree(BaseTree):

    def __init__(self, indexer=NodeDictIndexer()):
        super().__init__()
        self.indexer = indexer

    def on_insert(self, node):
        self.indexer.put(node.data, node)
        self.nodes_count += 1

    def get(self, key):
        return self.indexer.get(key)

    def on_remove(self, node):
        self.indexer.remove(node)
        self.nodes_count -= 1

    @abc.abstractmethod
    def _create_root_node(self, words, depth):
        raise NotImplementedError()

    @abc.abstractmethod
    def _create_node(self, node, words, depth):
        raise NotImplementedError()
