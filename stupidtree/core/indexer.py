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


class NodeIndexer(NodeIndexInterface):

    def __init__(self):
        self._dict = dict()

    def put(self, key, node, put_filter=None):
        if key in self._dict.keys():
            if put_filter is None or put_filter(node):
                self._dict[key].add(node)
            return
        self._dict[key] = set()
        if put_filter is None or put_filter(node):
            self._dict[key].add(node)

    def get(self, key):
        if key in self._dict.keys():
            return self._dict[key]
        return []

    def remove(self, key, rm_filter=None):
        if key not in self._dict.keys():
            return
        nodes = set()
        for n in self._dict[key]:
            if rm_filter is None or rm_filter(n):
                nodes.add(n)
        for n in nodes:
            self._dict[key].remove(n)
        nodes.clear()
