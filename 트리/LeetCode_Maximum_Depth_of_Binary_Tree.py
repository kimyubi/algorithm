# Definition for a binary tree node.
# Input: root = [3,9,20,null,null,15,7]
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0 

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1

            for _ in range(len(deque)):
                cur_root = queue.popleft()

                if cur_root.left:
                    queue.append(cur_root.left)

                if cur_root.right:
                    queue.append(cur_root.right)

        return depth

        