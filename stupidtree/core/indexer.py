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


class NodeIndexInterface(abc.ABC):
    """Index nodes in tree."""

    @abc.abstractmethod
    def put(self, key, node):
        """Add a node into indexer

        :param key:
        :param node:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, key):
        """Get all nodes match the `key`

        :param key: node's `data` field
        :return: A list of node
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, node):
        """Remove a node from indexer

        :param node: the node to be removed
        :return:
        """
        raise NotImplementedError()


class NodeDictIndexer(NodeIndexInterface):

    def __init__(self):
        self._dict = dict()

    def put(self, key, node):
        # if not key:
        #     raise ValueError("Argument key is NoneType.")
        if key in self._dict.keys():
            self._dict[key].add(node)
            return
        self._dict[key] = set()
        self._dict[key].add(node)

    def get(self, key):
        if key in self._dict.keys():
            return self._dict[key]
        return []

    def remove(self, node):
        key = node.data
        if not key:
            return
        if key in self._dict.keys():
            self._dict[key].remove(node)
