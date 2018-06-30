from .indexer import NodeDictIndexer
from .node import Node
import unittest


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
