# 993. Cousins in Binary Tree

# TC : O(n) where n is the number of nodes in the tree. In the worst case, we might need to visit all nodes.
# SC : O(n) for the queue in the worst case (a complete binary tree's last level has n/2 nodes).
# Did this code successfully run on Leetcode : yes

# Approach :
# We handle edge cases first: an empty tree or if either target value is at the root (in which case they can't be cousins).
# We initialize a queue for BFS traversal, where each element contains the node, its parent, and its depth.
# We set up variables to track the depth and parent of our target nodes x and y.
# We perform a BFS traversal:
    # For each node, we check if it matches either of our target values.
    # If it does, we store its depth and parent.
    # We add its children to the queue with updated parent and depth information.
    # We continue until we've found both x and y or exhausted the tree.
# Check if x and y are cousins: they must have the same depth but different parents.
# This approach efficiently handles the problem by using a single traversal to collect all the information we need about both nodes, and then making a simple comparison to determine if they're cousins.

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Edge case: empty tree or root is one of the values
        if not root or root.val == x or root.val == y:
            return False
        
        # Queue for BFS traversal - stores (node, parent, depth)
        queue = [(root, None, 0)]
        
        # Variables to store information about x and y
        x_depth, x_parent = -1, None
        y_depth, y_parent = -1, None
        
        # BFS traversal
        while queue and (x_depth == -1 or y_depth == -1):
            node, parent, depth = queue.pop(0)
            
            # Check if current node is x or y
            if node.val == x:
                x_depth, x_parent = depth, parent
            elif node.val == y:
                y_depth, y_parent = depth, parent
            
            # Add children to queue
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
        
        # Nodes are cousins if they have the same depth but different parents
        return x_depth == y_depth and x_parent != y_parent
        