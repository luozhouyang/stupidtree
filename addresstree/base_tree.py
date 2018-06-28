import abc

from .level import Level
from .node import AddressNode


class BaseTreeInterface(abc.ABC):

    @abc.abstractmethod
    def put(self, words):
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, key):
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, key, callback):
        raise NotImplementedError()

    @abc.abstractmethod
    def size(self):
        raise NotImplementedError()


class BaseTree(BaseTreeInterface):

    def __init__(self, level_offset=2, root=None):
        self.level_offset = level_offset
        if root is None:
            self.root = AddressNode("", None, None)
        else:
            self.root = root
        self.nodes_count = 1

    def put(self, words):
        if isinstance(words, list):
            self._put(self.root, words, 0)
        elif isinstance(words, str):
            self._put(self.root, words.split(","), 0)
        else:
            raise TypeError("Argument `words` must be in str or list Type.")

    def _put(self, node, words, depth):
        if depth == len(words):
            return
        child = AddressNode(words[depth], Level(depth + 2), node)
        for c in node.children:
            if c == child:
                self._put(c, words, depth + 1)
                return
        node.children.append(child)
        self.on_insert(child)
        self._put(child, words, depth + 1)

    @abc.abstractmethod
    def on_insert(self, node):
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, key):
        raise NotImplementedError()

    def remove(self, key, callback):
        if not key:
            return
        nodes = self.get(key)
        if not nodes or len(nodes) == 0:
            return
        for n in nodes:
            if callback(n):
                self._remove(n)

    def _remove(self, n):
        if not n:
            return
        for c in n.children:
            self._remove(c)
        if n.parent:
            n.parent.children.remove(n)
        self.on_remove(n)
        n.parent = None
        n = None

    @abc.abstractmethod
    def on_remove(self, node):
        raise NotImplementedError()

    def size(self):
        return self.nodes_count
