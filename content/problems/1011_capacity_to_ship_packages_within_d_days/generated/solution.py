from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flipped = []
        self.index = 0
        
        def dfs(node):
            if node is None:
                return True
            
            # Check if current node matches expected value in voyage
            if node.val != voyage[self.index]:
                return False
            
            self.index += 1
            
            # Check if we need to flip this node
            # If left child exists and doesn't match next expected value
            if (node.left is not None and 
                node.left.val != voyage[self.index]):
                # Flip: swap left and right children
                flipped.append(node.val)
                node.left, node.right = node.right, node.left
            
            # Continue DFS on left and right subtrees
            return dfs(node.left) and dfs(node.right)
        
        if dfs(root):
            return flipped
        else:
            return [-1]


# Helper function to build a binary tree from a list
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: root = [1,2], voyage = [2,1]
    root1 = build_tree([1, 2])
    voyage1 = [2, 1]
    result1 = solution.flipMatchVoyage(root1, voyage1)
    print(f"Example 1: {result1}")  # Expected: [-1]
    
    # Example 2: root = [1,2,3], voyage = [1,3,2]
    root2 = build_tree([1, 2, 3])
    voyage2 = [1, 3, 2]
    result2 = solution.flipMatchVoyage(root2, voyage2)
    print(f"Example 2: {result2}")  # Expected: [1]
    
    # Example 3: root = [1,2,3], voyage = [1,2,3]
    root3 = build_tree([1, 2, 3])
    voyage3 = [1, 2, 3]
    result3 = solution.flipMatchVoyage(root3, voyage3)
    print(f"Example 3: {result3}")  # Expected: []