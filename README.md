# stupidtree
A generic tree implementation in Python.


## Installation

From pypi:
```bash
pip install stupidtree
```

or clone this repo:
```bash
git clone https://github.com/luozhouyang/stupidtree
```

## Architecture

The design of this lib is flexible and expandable.

The module `stupidtree.core` has already defines the `Node` class, which works for most situations.  
Here is the `__init__` function's signature:
```python
def __init__(data, tag, parent):
    pass
```

For your special needs, you can inherit the `Node` class and override some functions as your need.

This module also defines the `BaseTree` class, which is the base class of all trees. It has already implemented the
interface `BaseTreeInterface`. This interface(or abstract class) contains these useful methods:
```python
class BaseTreeInterface(abc.ABC):

    def put(self, words):
        raise NotImplementedError()

    def remove(self, key, rm_filter):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError()
```  

**You can put nodes into the tree with any depth and any counts**.

For improving searching performance, a `Indexer` has been implemented. It is based on `dict`, using `hash` of keys to search nodes in O(1).    

Module `stupidtree.core` has implemented a tree `IndexedTree` that supports index. In most situations, the index will be helpful. And if you 
want to add another index, just inherit `NodeIndexInterface` and implements the abstract methods.

## Usage
The usage of `stupidtree` is quitely simple. You just need to put a string or a list into a constructed tree that derived from `BaseTree` or `IndexedTree`.  
Here is a example of Chinese address in `stupidtree.examples` package.  

For intuitive, I am showing you a few test examples:  

```python
import unittest

from stupidtree.examples.address.level import Level
from stupidtree.examples.address.pcd_tree import PCDTree


class TestPCDTree(unittest.TestCase):

    def test_put(self):
        tree = PCDTree()
        a0 = '浙江省 杭州市 西湖区'
        tree.put(a0)
        self.assertEqual(4, tree.size())
        tree.print()
        a1 = '浙江省 杭州市 江干区'
        tree.put(a1)
        self.assertEqual(5, tree.size())

        nodes = tree.get('浙江省')
        self.assertEqual(1, len(nodes))
        for n in nodes:
            self.assertEqual(Level.PROVINCE, n.tag)

    def test_remove(self):
        tree = PCDTree()
        a0 = '浙江省 杭州市 西湖区'
        tree.put(a0)
        a1 = '浙江省 杭州市 江干区'
        tree.put(a1)
        tree.print()

        tree.remove('江干区')
        self.assertEqual(4, tree.size())
        tree.print()

        tree.remove('浙江省')
        self.assertEqual(1, tree.size())
        tree.print()

        tree.remove('')
        print()
        tree.print()
        self.assertEqual(0, tree.size())


if __name__ == "__main__":
    unittest.main()
``` 

And here are the outputs:
```bash
+--
|    +--浙江省
|    |    +--杭州市
|    |    |    +--西湖区
.+--
|    +--浙江省
|    |    +--杭州市
|    |    |    +--西湖区
|    |    |    +--江干区
+--
|    +--浙江省
|    |    +--杭州市
|    |    |    +--西湖区
|    |    |    +--江干区
+--
|    +--浙江省
|    |    +--杭州市
|    |    |    +--西湖区
|    |    |    +--江干区

+--
|    +--浙江省
|    |    +--杭州市
|    |    |    +--西湖区
|    |    |    +--江干区
```  

## License  
```bash
MIT License

Copyright (c) 2018 luozhouyang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```  
