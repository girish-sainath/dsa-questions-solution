from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            # Base case: empty node is valid
            if not node:
                return True
            
            # Current node's value must be within (min_val, max_val)
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left and right subtrees
            # - Left subtree: upper bound becomes current node's value
            # - Right subtree: lower bound becomes current node's value
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        # Start with infinite bounds
        return validate(root, float('-inf'), float('inf'))


# ─── Helper to build tree from list ───────────────────────────────────────────
def build_tree(values: list) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list (None represents missing nodes)."""
    if not values or values[0] is None:
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


# ─── Test Cases ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([2, 1, 3], True),                          # Valid BST
        ([5, 1, 4, None, None, 3, 6], False),       # Right child 4 < root 5
        ([1], True),                                 # Single node
        ([5, 4, 6, None, None, 3, 7], False),       # 3 is in right subtree but < 5
        ([2, 2, 2], False),                          # Duplicate values (not valid BST)
        ([1, None, 1], False),                       # Duplicate values on right
    ]
    
    for i, (values, expected) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = solution.isValidBST(root)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i}: {status} | Input: {values} | Expected: {expected} | Got: {result}")