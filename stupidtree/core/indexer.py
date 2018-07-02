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
