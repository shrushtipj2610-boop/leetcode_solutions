class Solution:
    def getLeaves(self, root, leaf):
        if root is None:
            return

        if root.left is None and root.right is None:
            leaf.append(root.val)
            return

        self.getLeaves(root.left, leaf)
        self.getLeaves(root.right, leaf)

    def leafSimilar(self, root1, root2):
        leaf1 = []
        leaf2 = []

        self.getLeaves(root1, leaf1)
        self.getLeaves(root2, leaf2)

        return leaf1 == leaf2