from collections import defaultdict, deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # Step 1: Build an undirected graph from the binary tree
        # Also track which nodes are leaves and find the target node
        graph = defaultdict(list)
        leaves = set()
        
        def build_graph(node, parent):
            if not node:
                return
            # If it's a leaf node
            if not node.left and not node.right:
                leaves.add(node.val)
            # Add edge between parent and current node (undirected)
            if parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            # Recurse on children
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        build_graph(root, None)
        
        # Step 2: BFS from target node k to find the nearest leaf
        queue = deque([k])
        visited = {k}
        
        while queue:
            node_val = queue.popleft()
            
            # If this node is a leaf, return it
            if node_val in leaves:
                return node_val
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node_val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # Should never reach here for valid input
        return -1


# ==================== Helper Functions ====================

def build_tree(values):
    """Build a binary tree from a level-order list (None for missing nodes)."""
    if not values or values[0] is None:
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


# ==================== Test Cases ====================

def test():
    solution = Solution()
    
    # Test Case 1:
    # Tree:     1
    #          / \
    #         3   2
    # k = 1 → closest leaf is 2 or 3 (distance 1)
    root1 = build_tree([1, 3, 2])
    result1 = solution.findClosestLeaf(root1, 1)
    print(f"Test 1: {result1}")  # Expected: 2 or 3
    assert result1 in [2, 3], f"Expected 2 or 3, got {result1}"
    
    # Test Case 2:
    # Tree:     1
    #            \
    #             3
    #            /
    #           2
    # k = 1 → closest leaf is 2 (distance 2)
    root2 = build_tree([1, None, 3, None, None, 2])
    result2 = solution.findClosestLeaf(root2, 1)
    print(f"Test 2: {result2}")  # Expected: 2
    assert result2 == 2, f"Expected 2, got {result2}"
    
    # Test Case 3:
    # Tree:      1
    #           / \
    #          2   3
    #         /   / \
    #        4   5   6
    #       /
    #      7
    #     /
    #    8
    # k = 4 → closest leaf is 8 (distance 2) or go up to 2 → 1 → 3 → 5/6
    # Distance to 8 = 1, to 7 = 1... wait 7 has child 8, so 7 is not a leaf
    # Leaves: 8, 5, 6
    # From 4: 4->7->8 = distance 2
    # From 4: 4->2->1->3->5 = distance 4, 4->2->1->3->6 = distance 4
    # Closest leaf is 8 at distance 2
    root3 = build_tree([1, 2, 3, 4, None, 5, 6, 7, None, None, None, None, None, 8])
    result3 = solution.findClosestLeaf(root3, 4)
    print(f"Test 3: {result3}")  # Expected: 8
    
    # Test Case 4: Single node (root is a leaf)
    root4 = build_tree([1])
    result4 = solution.findClosestLeaf(root4, 1)
    print(f"Test 4: {result4}")  # Expected: 1
    assert result4 == 1, f"Expected 1, got {result4}"
    
    print("\nAll test cases passed!")

if __name__ == "__main__":
    test()