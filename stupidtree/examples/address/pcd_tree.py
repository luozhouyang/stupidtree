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

from stupidtree.core.indexed_tree import IndexedTree
from stupidtree.core.indexer import NodeDictIndexer
from stupidtree.examples.address.level import Level
from stupidtree.examples.address.node import AddressNode


class PCDInterface(abc.ABC):
    @abc.abstractmethod
    def provinces(self):
        """
        Get province level nodes
        :return: a set of nodes
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def cities(self):
        """
        Get city level nodes
        :return: a set of nodes
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def districts(self):
        """
        Get district level nodes
        :return: a set of nodes
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def contains(self, key):
        """
        If the tree contains nodes whose tag equals `key`
        :param key: node's tag
        :return: a set of nodes
        """
        raise NotImplementedError()


class PCDTree(IndexedTree, PCDInterface):
    """
    Chinese address tree. Addresses contains Province, City and District levels.
    PCD are Province, City and District.
    """

    def __init__(self, indexer=NodeDictIndexer()):
        """
        Construct tree.
        :param indexer: nodes' indexer
        """
        super().__init__(indexer=indexer)
        self.provinces = set()
        self.cities = set()
        self.districts = set()

    def on_insert(self, node):
        super().on_insert(node)
        if node.tag == Level.COUNTRY:
            return
        if node.tag == Level.PROVINCE:
            self.provinces.add(node)
            return
        if node.tag == Level.CITY:
            self.cities.add(node)
            return
        if node.tag == Level.DISTRICT:
            self.districts.add(node)
            return

    def on_remove(self, node):
        super().on_remove(node)
        if node.tag == Level.COUNTRY:
            return
        if node.tag == Level.PROVINCE:
            self.provinces.remove(node)
            return
        if node.tag == Level.CITY:
            self.cities.remove(node)
            return
        if node.tag == Level.DISTRICT:
            self.districts.remove(node)
            return

    def _create_root_node(self, words, depth):
        return AddressNode(data='', level=Level.COUNTRY, parent=None)

    def _create_node(self, node, words, depth):
        return AddressNode(data=words[depth], level=Level(depth + 2),
                           parent=node)

    def provinces(self):
        return self.provinces

    def cities(self):
        return self.cities

    def districts(self):
        return self.districts

    def contains(self, key):
        nodes = self.get(key)
        if not nodes:
            return False
        return len(nodes) > 0
