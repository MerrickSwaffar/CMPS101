import copy
from hw6 import BSTree
import unittest
from io import StringIO
import sys

class BSTreeUnittest(unittest.TestCase):
    def setUp(self):
        """ instantiate the binary search tree """
        self.mytree = BSTree()
        self.treedata = [("Foxtrot",20), ("Delta",15), ("Echo",17),
                         ("Alpha",5), ("Bravo",10), ("Charlie",12),
                         ("Golf",22), ("Hotel",25), ("India",27)]

    def test_delete(self):
        """ test the deletion procedure """
        for element in self.treedata:
            self.mytree.insert(key=element[0], value=element[1])

        self.mytree.delete("Golf")
        self.mytree.delete("Delta")
        self.mytree.delete("Echo")

        self.treedata.sort()

        self.treedata.remove(("Golf", 22))
        self.treedata.remove(("Delta",15))
        self.treedata.remove(("Echo",17))

        old_data = copy.deepcopy(self.treedata)

        old_stdout = sys.stdout

        output = StringIO()
        sys.stdout = output

        self.mytree.inOrderTraversal()

        result = output.getvalue()
        sys.stdout = old_stdout

        result = result.split("\n")

        for i in range(len(self.treedata)):
            if old_data[i][0] in result[i]:
                self.treedata.remove(old_data[i])

        self.assertEqual(len(self.treedata), 0)


    def test_inOrderTraversal(self):
        """ test the traversal methods """
        for element in self.treedata:
            self.mytree.insert(key=element[0], value=element[1])

        self.treedata.sort()
        old_data = copy.deepcopy(self.treedata)
        old_stdout = sys.stdout

        output = StringIO()
        sys.stdout = output

        self.mytree.inOrderTraversal()

        result = output.getvalue()
        sys.stdout = old_stdout

        result = result.split("\n")

        for i in range(len(self.treedata)):
            if old_data[i][0] in result[i]:
                self.treedata.remove(old_data[i])

        self.assertEqual(len(self.treedata), 0)

if __name__ == '__main__':
    unittest.main()