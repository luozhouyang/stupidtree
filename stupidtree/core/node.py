# Copyright (c) 2018 luozhouyang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
