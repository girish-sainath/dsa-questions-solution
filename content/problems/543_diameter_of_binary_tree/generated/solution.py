from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def height(node: Optional[TreeNode]) -> int:
            """
            Returns the height of the subtree rooted at node.
            Also updates max_diameter as a side effect.
            """
            if node is None:
                return 0
            
            # Recursively get height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Diameter at current node = left_height + right_height
            # Update global maximum if this is larger
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return height of current node (1 + max of left/right heights)
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.max_diameter


# Helper function to build tree from list (level-order)
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
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
    
    # Example 1: root = [1,2,3,4,5], Expected: 3
    root1 = build_tree([1, 2, 3, 4, 5])
    result1 = solution.diameterOfBinaryTree(root1)
    print(f"Example 1: {result1}")  # Output: 3
    
    # Example 2: root = [1,2], Expected: 1
    root2 = build_tree([1, 2])
    result2 = solution.diameterOfBinaryTree(root2)
    print(f"Example 2: {result2}")  # Output: 1
    
    # Edge case: Single node
    root3 = build_tree([1])
    result3 = solution.diameterOfBinaryTree(root3)
    print(f"Single node: {result3}")  # Output: 0
    
    # Linear tree: [1,2,null,3,null,4]
    root4 = build_tree([1, 2, None, 3, None, 4])
    result4 = solution.diameterOfBinaryTree(root4)
    print(f"Linear tree: {result4}")  # Output: 3