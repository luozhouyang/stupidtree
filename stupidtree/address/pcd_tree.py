from stupidtree.core.indexed_tree import IndexedTree
from stupidtree.address.level import Level
import abc


class PCDInterface(abc.ABC):
    @abc.abstractmethod
    def provinces(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def cities(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def districts(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def contains(self, key):
        raise NotImplementedError()


# TODO(luozhouyang) Refactor PCDTree
class PCDTree(IndexedTree, PCDInterface):

    def __init__(self,
                 insert_callback=None,
                 remove_callback=None,
                 level_offset=2,
                 root=None):
        super().__init__(level_offset, root)
        self.insert_callback = insert_callback
        self.remove_callback = remove_callback
        self.provinces = set()
        self.cities = set()
        self.districts = set()

    def on_insert(self, node):
        if not node:
            raise TypeError("Argument `node` is NoneType.")
        if node.level == Level.COUNTRY:
            print("Country node %s inserted." % node.data)
        elif node.level == Level.PROVINCE:
            self.provinces.add(node)
            self.nodes_count += 1
            self.indexer.put(node.data, node, self.insert_callback)
        elif node.level == Level.CITY:
            self.cities.add(node)
            self.nodes_count += 1
            self.indexer.put(node.data, node, self.insert_callback)
        elif node.level == Level.DISTRICT:
            self.districts.add(node)
            self.nodes_count += 1
            self.indexer.put(node.data, node, self.insert_callback)
        else:
            raise ValueError(
                "Unknown level %s in node %s" % (node.level, node.data))

    def on_remove(self, node):
        if not node:
            raise TypeError("Argument `node` is NoneType.")
        if node.level == Level.COUNTRY:
            self.nodes_count -= 1
            self.indexer.remove(node.data, self.remove_callback)
        elif node.level == Level.PROVINCE:
            self.provinces.add(node)
            self.nodes_count += 1
            self.indexer.put(node.data, node, self.remove_callback)
        elif node.level == Level.CITY:
            self.cities.add(node)
            self.nodes_count += 1
            self.indexer.put(node.data, node, self.remove_callback)
        elif node.level == Level.DISTRICT:
            self.districts.add(node)
            self.nodes_count += 1
            self.indexer.put(node.data, node, self.remove_callback)
        else:
            raise ValueError(
                "Unknown level %s in node %s" % (node.level, node.data))

    def _create_root_node(self, words, depth):
        pass

    def _create_node(self, node, words, depth):
        pass

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
