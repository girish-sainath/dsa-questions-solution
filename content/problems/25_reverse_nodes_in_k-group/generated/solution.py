class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy  # Tail of the previous reversed group

        while True:
            # Step 1: Check if there are k nodes remaining
            kth_node = self.get_kth_node(prev_group_tail, k)
            if not kth_node:
                break  # Fewer than k nodes remaining, stop

            # Step 2: Identify the start and end of current group
            group_start = prev_group_tail.next
            next_group_start = kth_node.next

            # Step 3: Reverse k nodes in the current group
            prev = next_group_start  # After reversing, group_start points to next_group_start
            curr = group_start

            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Step 4: Connect previous group's tail to new head of reversed group
            prev_group_tail.next = kth_node  # kth_node is now the head of reversed group
            prev_group_tail = group_start    # group_start is now the tail of reversed group

        return dummy.next

    def get_kth_node(self, curr: ListNode, k: int) -> ListNode:
        """Move k steps from curr and return the node, or None if not enough nodes."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: k=2
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseKGroup(head1, 2)
    print(f"Test 1 - Input: [1,2,3,4,5], k=2")
    print(f"Output: {linked_list_to_list(result1)}")  # Expected: [2,1,4,3,5]

    # Test Case 2: k=3
    head2 = create_linked_list([1, 2, 3, 4, 5])
    result2 = solution.reverseKGroup(head2, 3)
    print(f"\nTest 2 - Input: [1,2,3,4,5], k=3")
    print(f"Output: {linked_list_to_list(result2)}")  # Expected: [3,2,1,4,5]

    # Test Case 3: k=1 (no reversal)
    head3 = create_linked_list([1, 2, 3, 4, 5])
    result3 = solution.reverseKGroup(head3, 1)
    print(f"\nTest 3 - Input: [1,2,3,4,5], k=1")
    print(f"Output: {linked_list_to_list(result3)}")  # Expected: [1,2,3,4,5]

    # Test Case 4: k equals list length
    head4 = create_linked_list([1, 2, 3, 4, 5])
    result4 = solution.reverseKGroup(head4, 5)
    print(f"\nTest 4 - Input: [1,2,3,4,5], k=5")
    print(f"Output: {linked_list_to_list(result4)}")  # Expected: [5,4,3,2,1]

    # Test Case 5: Single node
    head5 = create_linked_list([1])
    result5 = solution.reverseKGroup(head5, 1)
    print(f"\nTest 5 - Input: [1], k=1")
    print(f"Output: {linked_list_to_list(result5)}")  # Expected: [1]