from .base_tree import BaseTree
from .indexer import NodeDictIndexer
import abc


class IndexedTree(BaseTree):

    def __init__(self, indexer=NodeDictIndexer()):
        super().__init__()
        self.indexer = indexer

    def on_insert(self, node):
        self.nodes_count += 1
        self.indexer.put(node.data, node)

    def get(self, key):
        return self.indexer.get(key)

    def on_remove(self, node):
        self.nodes_count -= 1
        self.indexer.remove(node)

    @abc.abstractmethod
    def _create_root_node(self, words, depth):
        raise NotImplementedError()

    @abc.abstractmethod
    def _create_node(self, node, words, depth):
        raise NotImplementedError()
