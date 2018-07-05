import unittest

from stupidtree.address.pcd_tree import PCDTree
from stupidtree.address.level import Level


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
