class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy head node to simplify edge cases
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists until both are exhausted and no carry remains
        while l1 is not None or l2 is not None or carry != 0:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit and append to result list
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if available
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return dummy_head.next


# ===================== Helper Functions =====================
def create_linked_list(nums: list) -> ListNode:
    """Create a linked list from a list of integers."""
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def linked_list_to_list(node: ListNode) -> list:
    """Convert a linked list to a list of integers."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ===================== Test Cases =====================
def run_tests():
    solution = Solution()
    
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),       # 342 + 465 = 807
        ([0], [0], [0]),                            # 0 + 0 = 0
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),  # Large numbers
        ([1], [9, 9], [0, 0, 1]),                  # 1 + 99 = 100
        ([5], [5], [0, 1]),                         # 5 + 5 = 10
    ]
    
    print("=" * 55)
    print(f"{'Test':<6} {'l1':<20} {'l2':<15} {'Expected':<15} {'Result':<15} {'Pass'}")
    print("=" * 55)
    
    for i, (l1_vals, l2_vals, expected) in enumerate(test_cases, 1):
        l1 = create_linked_list(l1_vals)
        l2 = create_linked_list(l2_vals)
        result_node = solution.addTwoNumbers(l1, l2)
        result = linked_list_to_list(result_node)
        
        passed = result == expected
        status = "✅" if passed else "❌"
        print(f"{i:<6} {str(l1_vals):<20} {str(l2_vals):<15} {str(expected):<15} {str(result):<15} {status}")
    
    print("=" * 55)


if __name__ == "__main__":
    run_tests()