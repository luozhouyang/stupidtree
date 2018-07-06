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

from stupidtree.core.node import Node


class BaseTreeInterface(abc.ABC):
    """A interface defines basic abilities a tree has."""

    @abc.abstractmethod
    def put(self, words):
        """Put a list of string or a single SPACE separated string to tree.

        :param words: If it is a list of string, each word in that will be inserted
                into tree. If it is a SPACE separated string, it will be split
                to a list of string and then insert these words to the tree.
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, key):
        """Get all the nodes in the tree whose `data` field equals the `key`.

        :param key: The key to match.
        :return: A list of `AddressNode` objects if found, or empty list.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, key, rm_filter=None):
        """Remove nodes whose `data` field euqls the `key` from the tree.

        If not found any node by the `key` in the tree, then do noting.

        If found node(s), the caller can decide whether remove the node or not
        using the `rm_filter` argument, whose signature is:
        ```python
        def callback(node)
            if ...:
                return True
            return False
        ```
        If `callback` returns `True`, the node will be removed,
        or returns `False', the node will be reserved.

        If `callback` is None, each node matched will be removed.
        :param key: The key to match.
        :param rm_filter: A callback function to decide whether remove the node
            or not.This is helpful when there has multi nodes that
            match the `key`.
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def size(self):
        """The total number of nodes in the tree."""
        raise NotImplementedError()


class BaseTree(BaseTreeInterface):

    def __init__(self):
        self.root = None
        self.nodes_count = 0

    def put(self, words):
        if isinstance(words, list):
            self._put(self.root, words, 0)
        elif isinstance(words, str):
            self._put(self.root, words.split(" "), 0)
        else:
            raise TypeError("Argument `words` must be SPACE "
                            "separated str or list Type.")

    def _put(self, node, words, depth):
        if not node:
            node = self._create_root_node(words, depth)
            self.root = node
            assert node
            self.on_insert(node)
        if depth == len(words):
            return
        # child = AddressNode(words[depth], Level(depth + 2), node)
        child = self._create_node(node, words, depth)
        assert isinstance(child, Node)
        for c in node.children:
            if c == child:
                self._put(c, words, depth + 1)
                return
        child.parent = node
        node.children.append(child)
        self.on_insert(child)
        self._put(child, words, depth + 1)

    @abc.abstractmethod
    def _create_root_node(self, words, depth):
        """Create the root node.

        :param words: words that to be inserted
        :param depth: index of current word in words
        :return: A root node. Can not be NoneType
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def _create_node(self, node, words, depth):
        """Create node

        :param node: parent node
        :param words: words to be inserted
        :param depth: index of current word in words
        :return: A node. Can not be NoneType
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def on_insert(self, node):
        """Notify node insertion

        :param node: the node to be inserted.
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, key):
        raise NotImplementedError()

    def remove(self, key, rm_filter=None):
        nodes = self.get(key)
        if not nodes or len(nodes) == 0:
            return
        for n in nodes.copy():
            if not rm_filter or rm_filter(n):
                self._remove(n)

    def _remove(self, n):
        for c in n.children.copy():
            self._remove(c)
        self.on_remove(n)
        if n.parent:
            n.parent.children.remove(n)
        n.parent = None

    @abc.abstractmethod
    def on_remove(self, node):
        """Notify node remove

        :param node: the node to be removed
        :return:
        """
        raise NotImplementedError()

    def size(self):
        return self.nodes_count

    def print(self):
        self._print(self.root, 0)

    def _print(self, node, depth):
        if depth == 0:
            print("+--" + node.data)
        for c in node.children:
            print("|    " * (depth + 1) + "+--" + c.data)
            self._print(c, depth + 1)
