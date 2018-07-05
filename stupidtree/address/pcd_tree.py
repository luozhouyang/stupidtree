from stupidtree.core.indexed_tree import IndexedTree
from stupidtree.address.level import Level
from stupidtree.core.indexer import NodeDictIndexer
from stupidtree.address.node import AddressNode
import abc


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
