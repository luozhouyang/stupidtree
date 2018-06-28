import abc


class NodeIndexInterface(abc.ABC):

    @abc.abstractmethod
    def put(self, key, node):
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, key):
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, key, callback):
        raise NotImplementedError()


class NodeIndexer(NodeIndexInterface):

    def __init__(self):
        self._dict = dict()

    def put(self, key, node, callback=None):
        if key in self._dict.keys():
            if callback is None or callback(node):
                self._dict[key].add(node)
            return
        self._dict[key] = set()
        if callback is None or callback(node):
            self._dict[key].add(node)

    def get(self, key):
        if key in self._dict.keys():
            return self._dict[key]
        return []

    def remove(self, key, callback=None):
        if key not in self._dict.keys():
            return
        nodes = set()
        for n in self._dict[key]:
            if callback is None or callback(n):
                nodes.add(n)
        for n in nodes:
            self._dict[key].remove(n)
        nodes.clear()
