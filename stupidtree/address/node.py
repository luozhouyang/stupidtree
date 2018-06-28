class AddressNode(object):

    def __init__(self, data, level, parent):
        self.data = data
        self.level = level
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
        return hash((self.data, self.level, self.parent))

    def __eq__(self, other):
        if not other:
            return False
        if not isinstance(other, AddressNode):
            return False
        if self.data != other.data:
            return False
        if self.level != other.level:
            return False
        if self.parent != other.parent:
            return False
        return True
