# 297 Serialize and Deserialize Binary Tree

# BFS level by level

# DFS Preorder Traversal


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        val = data.split(",")
        self.i = 0

        def dfs():
            if val[self.i] == "null":
                self.i += 1
                return None
            nodee = TreeNode(int(val[self.i]))
            self.i += 1
            nodee.left = dfs()
            nodee.right = dfs()

            return nodee
        return dfs()
