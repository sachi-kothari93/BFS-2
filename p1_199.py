# 199. Binary Tree Right Side View

# TC : O(n) where n is the number of nodes in the tree. Each node is processed exactly once.
# SC : O(d) where d is the maximum width of the tree. In the worst case for a complete binary tree, the maximum width is n/2, so space complexity is O(n).
# Did this code successfully run on Leetcode : yes

# Approach :
# We first handle the edge case of an empty tree by returning an empty list.
# We initialize our result list to store the values of nodes visible from the right side.
# We set up a queue for level order traversal, starting with the root node.
# The main loop continues as long as there are nodes to process in the queue.
# For each level:
    # We determine how many nodes are at the current level.
    # We process each node at the current level one by one.
    # For each node, if it's the rightmost node of the level (i.e., the last one we process), we add its value to our result.
    # We add the node's children to the queue for processing in the next level.
# After processing all levels, we return the final result containing all the rightmost nodes.
# This approach ensures we get the rightmost node from each level, which is exactly what we need for the right side view of the tree.

from collections import deque
from typing import Collection, List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: empty tree
        if not root:
            return []
        
        # Result list to store right side view nodes
        result = []
        
        # Queue for level order traversal
        queue = Collection.deque([root])
        
        # Level order traversal
        while queue:
            # Get the size of the current level
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                # Get the next node
                node = queue.popleft()
                
                # If this is the rightmost node of the level, add to result
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result