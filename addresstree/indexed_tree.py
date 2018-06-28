from .base_tree import BaseTree
from .indexer import NodeIndexer


class IndexedTree(BaseTree):

    def __init__(self,
                 insert_callback=None,
                 remove_callback=None,
                 level_offset=2, root=None):
        self.insert_callback = insert_callback
        self.remove_callback = remove_callback
        self.indexer = NodeIndexer()
        super().__init__(level_offset, root)

    def on_insert(self, node):
        self.nodes_count += 1
        self.indexer.put(node.data, node, self.insert_callback)

    def get(self, key):
        return self.indexer.get(key)

    def on_remove(self, node):
        self.nodes_count -= 1
        self.indexer.remove(node.data, self.remove_callback)
