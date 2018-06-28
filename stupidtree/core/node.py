class Node(object):
    def __init__(self, data, tag, parent):
        self.data = data
        self.tag = tag
        self.parent = parent
        self.children = list()

    def address(self):
        addr = self.data if self.data else ""
        p = self.parent
        while p:
            addr = addr + " " + p.name
            p = p.parent
        return addr.strip()

    def csv_address(self):
        addr = self.data if self.data else ""
        p = self.parent
        while p:
            addr = addr + "," + p.name
            p = p.parent
        return addr.strip()

    def __hash__(self):
        return hash((self.data, self.tag, self.parent))

    def __eq__(self, other):
        if not other:
            return False
        if not isinstance(other, Node):
            return False
        if self.data != other.data:
            return False
        if self.tag != other.tag:
            return False
        if self.parent != other.parent:
            return False
        return True
