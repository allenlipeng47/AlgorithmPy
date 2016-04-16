class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = []
        self.loadLeft(root)

    def loadLeft(self, root):
        while root is not None:
            self.s.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.s


    def next(self):
        """
        :rtype: int
        """
        curr = self.s.pop(-1)
        self.loadLeft(curr.right)
        return curr.val
