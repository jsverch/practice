from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.boundary = list()
        self.l_b = list()
        self.r_b = list()
        self.lfs = list()

    def leftb(self, n: TreeNode):
        while n:
            if not self.isleaf(n):
                self.l_b.append(n.val)
            if n.left:
                n = n.left
            else:
                n = n.right
        return

    def rightb(self, n: TreeNode):
        while n:
            if not self.isleaf(n):
                self.r_b.append(n.val)
            if n.right:
                n = n.right
            else:
                n = n.left
        return

    def isleaf(self, n: TreeNode):
        if not n.left and not n.right:
            return 1
        else:
            return 0

    def leaves(self, n: TreeNode):
        if self.isleaf(n):
            self.lfs.append(n.val)

        if n.left:
            self.leaves(n.left)

        if n.right:
            self.leaves(n.right)

        return self.lfs

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if self.isleaf(root):
            return [root.val]
        self.boundary.append(root.val)
        if root.left:
            self.leftb(root.left)
        self.leaves(root)
        if root.right:
            self.rightb(root.right)
        self.r_b.reverse()
        return self.boundary + self.l_b + self.lfs + self.r_b


root = TreeNode()
root.val = 1
# n_2 = TreeNode()
# n_2.val = 2
# n_3 = TreeNode()
# n_3.val = 3
# n_4 = TreeNode()
# n_4.val = 4
# n_5 = TreeNode()
# n_5.val = 5
# n_6 = TreeNode()
# n_6.val = 6
# n_7 = TreeNode()
# n_7.val = 7
#
# root.left = n_2
# root.right = n_3
# n_2.left = n_4
# n_2.right = n_5
# n_5.left = n_7
# n_3.left = n_6


obj = Solution()

print(obj.boundaryOfBinaryTree(root))

# print(obj.leaves(root))
