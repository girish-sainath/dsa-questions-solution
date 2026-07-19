class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find the Lowest Common Ancestor of two nodes in a binary tree.
        
        Args:
            root: Root node of the binary tree
            p: First target node
            q: Second target node
        
        Returns:
            The LCA node
        
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(h) - recursion stack where h is tree height
                         O(n) worst case for skewed tree, O(log n) for balanced
        """
        # Base case: if root is None, p, or q → return root
        if root is None or root == p or root == q:
            return root
        
        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both sides found a node → current root is the LCA
        if left and right:
            return root
        
        # Otherwise, return whichever side found a node
        return left if left else right


# ─── Helper to build tree from level-order list ───────────────────────────────
def build_tree(values):
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


def find_node(root, val):
    """Find and return the node with the given value."""
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


# ─── Test Cases ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: LCA of 5 and 1 → expected 3
    tree1 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p1 = find_node(tree1, 5)
    q1 = find_node(tree1, 1)
    result1 = solution.lowestCommonAncestor(tree1, p1, q1)
    print(f"Test 1 - LCA of {p1.val} and {q1.val}: {result1.val}")  # Expected: 3
    
    # Test Case 2: LCA of 5 and 4 → expected 5
    tree2 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p2 = find_node(tree2, 5)
    q2 = find_node(tree2, 4)
    result2 = solution.lowestCommonAncestor(tree2, p2, q2)
    print(f"Test 2 - LCA of {p2.val} and {q2.val}: {result2.val}")  # Expected: 5
    
    # Test Case 3: LCA of 1 and 2 → expected 1
    tree3 = build_tree([1, 2])
    p3 = find_node(tree3, 1)
    q3 = find_node(tree3, 2)
    result3 = solution.lowestCommonAncestor(tree3, p3, q3)
    print(f"Test 3 - LCA of {p3.val} and {q3.val}: {result3.val}")  # Expected: 1