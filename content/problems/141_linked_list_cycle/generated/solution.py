from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if a linked list has a cycle using Floyd's Algorithm.
        
        Time Complexity: O(n) - in worst case, we traverse all nodes
        Space Complexity: O(1) - only two pointers used
        """
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2
            
            if slow is fast:          # Cycle detected
                return True
        
        return False  # No cycle found


# ============================================================
# Helper function to create linked list with optional cycle
# ============================================================
def create_linked_list(values: list, pos: int) -> Optional[ListNode]:
    """Creates a linked list with an optional cycle at position pos."""
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    
    # Link all nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if pos is valid
    if pos >= 0:
        nodes[-1].next = nodes[pos]  # Tail points to node at pos
    
    return nodes[0]


# ============================================================
# Test Cases
# ============================================================
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "values": [3, 2, 0, -4],
            "pos": 1,
            "expected": True,
            "description": "Cycle at position 1 (tail -> node[1])"
        },
        {
            "values": [1, 2],
            "pos": 0,
            "expected": True,
            "description": "Cycle at position 0 (tail -> node[0])"
        },
        {
            "values": [1],
            "pos": -1,
            "expected": False,
            "description": "Single node, no cycle"
        },
        {
            "values": [],
            "pos": -1,
            "expected": False,
            "description": "Empty list"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "pos": -1,
            "expected": False,
            "description": "No cycle in 5-node list"
        },
    ]
    
    print("=" * 60)
    print("Testing Linked List Cycle Detection")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        head = create_linked_list(test["values"], test["pos"])
        result = solution.hasCycle(head)
        status = "✅ PASS" if result == test["expected"] else "❌ FAIL"
        
        print(f"\nTest {i}: {test['description']}")
        print(f"  Input : values={test['values']}, pos={test['pos']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {status}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    run_tests()