"""
 题目描述：
    给定一个二叉树，找出其最大深度。
    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    示例：
        给定二叉树 [3,9,20,null,null,15,7]，
            3
           / \
          9  20
            /  \
           15   7
"""


# 树类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def way_one(self, root) -> int:         # 深度优先搜索算法
    if root is None:
        return 0
    else:
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1