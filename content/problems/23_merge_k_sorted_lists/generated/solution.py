import heapq
from typing import List, Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to store (value, index, node)
        # index is used as tiebreaker to avoid comparing ListNode objects
        heap = []
        
        # Initialize heap with head of each linked list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Dummy head node to simplify result construction
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            # Extract the node with minimum value
            val, i, node = heapq.heappop(heap)
            
            # Add it to the result list
            current.next = node
            current = current.next
            
            # Push the next node of the extracted node (if exists)
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next


# ─────────────────────────────────────────
# Helper Functions for Testing
# ─────────────────────────────────────────

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """Convert a list of values to a linked list."""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    """Convert a linked list to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ─────────────────────────────────────────
# Test Cases
# ─────────────────────────────────────────

def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "input": [[1, 4, 5], [1, 3, 4], [2, 6]],
            "expected": [1, 1, 2, 3, 4, 4, 5, 6]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [[]],
            "expected": []
        },
        {
            "input": [[1], [0]],
            "expected": [0, 1]
        },
        {
            "input": [[-10, -5, 0], [-8, -3, 2], [-6, 1, 4]],
            "expected": [-10, -8, -6, -5, -3, 0, 1, 2, 4]
        }
    ]
    
    for i, test in enumerate(test_cases):
        # Build linked lists from input
        lists = [build_linked_list(lst) for lst in test["input"]]
        
        # Run solution
        result_node = solution.mergeKLists(lists)
        result = linked_list_to_list(result_node)
        
        status = "✅ PASSED" if result == test["expected"] else "❌ FAILED"
        print(f"Test {i + 1}: {status}")
        print(f"  Input:    {test['input']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got:      {result}")
        print()


if __name__ == "__main__":
    run_tests()