from collections import deque
from typing import Optional, List


# Definition for a binary tree node
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
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)  # Number of nodes at current level
            
            for i in range(level_size):
                node = queue.popleft()
                
                # If it's the last node in this level, add to result
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result


# Helper function to build tree from list
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: root = [1,2,3,null,5,null,4]
    root1 = build_tree([1, 2, 3, None, 5, None, 4])
    print(f"Example 1: {solution.rightSideView(root1)}")  # Expected: [1, 3, 4]
    
    # Example 2: root = [1,2,3,4,null,null,null,5]
    root2 = build_tree([1, 2, 3, 4, None, None, None, 5])
    print(f"Example 2: {solution.rightSideView(root2)}")  # Expected: [1, 3, 4, 5]
    
    # Example 3: root = [1,null,3]
    root3 = build_tree([1, None, 3])
    print(f"Example 3: {solution.rightSideView(root3)}")  # Expected: [1, 3]
    
    # Example 4: root = []
    root4 = build_tree([])
    print(f"Example 4: {solution.rightSideView(root4)}")  # Expected: []