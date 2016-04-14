class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution(object):

    def __init__(self):
        self.maxDepth = 0

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.maxDepth = 0
        self.helper(root, 1, ans)
        return ans

    def helper(self, root, currDepth, ans):
        if root is None:
            return
        if currDepth > self.maxDepth:
            ans.append(root.val)
            self.maxDepth = currDepth
        self.helper(root.right, currDepth + 1, ans)
        self.helper(root.left, currDepth + 1, ans)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t1.left = t2; t1.right = t3
t2.left = t4
t4.left = t6
t3.left = t5
s = Solution()
print (s.rightSideView(t1))
