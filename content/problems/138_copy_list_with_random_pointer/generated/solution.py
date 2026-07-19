from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Deep copy a linked list with random pointers using HashMap approach.
        
        Args:
            head: Head node of the original linked list
            
        Returns:
            Head node of the deep copied linked list
        """
        if not head:
            return None
        
        # HashMap to store mapping: original_node -> copied_node
        node_map = {}
        
        # First Pass: Create all new nodes and store in HashMap
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        # Second Pass: Assign next and random pointers
        current = head
        while current:
            # Set next pointer
            if current.next:
                node_map[current].next = node_map[current.next]
            
            # Set random pointer
            if current.random:
                node_map[current].random = node_map[current.random]
            
            current = current.next
        
        return node_map[head]


# ==================== Helper Functions for Testing ====================

def build_linked_list(data: list) -> Optional[Node]:
    """
    Build a linked list from a list of [val, random_index] pairs.
    
    Args:
        data: List of [val, random_index] pairs
        
    Returns:
        Head node of the constructed linked list
    """
    if not data:
        return None
    
    # Create all nodes first
    nodes = [Node(val) for val, _ in data]
    
    # Set next and random pointers
    for i, (_, random_index) in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    
    return nodes[0]


def linked_list_to_list(head: Optional[Node]) -> list:
    """
    Convert a linked list to a list of [val, random_index] pairs.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        List of [val, random_index] pairs
    """
    if not head:
        return []
    
    # First, map each node to its index
    node_to_index = {}
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1
    
    # Then, build the result list
    result = []
    current = head
    while current:
        random_index = node_to_index[current.random] if current.random else None
        result.append([current.val, random_index])
        current = current.next
    
    return result


# ==================== Test Cases ====================

def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "input": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            "expected": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        },
        {
            "input": [[1, 1], [2, 1]],
            "expected": [[1, 1], [2, 1]]
        },
        {
            "input": [[3, None], [3, 0], [3, None]],
            "expected": [[3, None], [3, 0], [3, None]]
        },
        {
            "input": [],  # Empty list
            "expected": []
        }
    ]
    
    print("=" * 60)
    print("Testing Copy List with Random Pointer")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        head = build_linked_list(test["input"])
        result_head = solution.copyRandomList(head)
        result = linked_list_to_list(result_head)
        
        # Verify deep copy: no shared nodes between original and copy
        if head and result_head:
            original_nodes = set()
            current = head
            while current:
                original_nodes.add(id(current))
                current = current.next
            
            is_deep_copy = True
            current = result_head
            while current:
                if id(current) in original_nodes:
                    is_deep_copy = False
                    break
                current = current.next
        else:
            is_deep_copy = True
        
        status = "✅ PASSED" if result == test["expected"] and is_deep_copy else "❌ FAILED"
        print(f"\nTest {i}: {status}")
        print(f"  Input:     {test['input']}")
        print(f"  Expected:  {test['expected']}")
        print(f"  Got:       {result}")
        print(f"  Deep Copy: {is_deep_copy}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_tests()