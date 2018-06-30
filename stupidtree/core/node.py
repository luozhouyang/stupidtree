class Node(object):
    def __init__(self, data, tag, parent):
        self.data = data
        self.tag = tag
        self.parent = parent
        self.children = list()

    def path_value(self):
        value = self.data if self.data else ""
        p = self.parent
        while p:
            value = value + " " + p.data
            p = p.parent
        return value.strip()

    def csv_path_value(self):
        value = self.data if self.data else ""
        p = self.parent
        while p:
            value = value + "," + p.data
            p = p.parent
        return value.strip()

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
