class Node:
    """Doubly Linked List Node"""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize LRU Cache with dummy head and tail nodes.
        
        Structure: head <-> [LRU ... MRU] <-> tail
        - head.next = LRU (least recently used)
        - tail.prev = MRU (most recently used)
        """
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Dummy head and tail nodes to avoid edge cases
        self.head = Node()  # Left boundary (LRU side)
        self.tail = Node()  # Right boundary (MRU side)
        
        # Connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_to_tail(self, node: Node) -> None:
        """Insert a node right before the tail (most recently used position)."""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        """
        Return value if key exists, else -1.
        Move accessed node to tail (most recently used).
        Time Complexity: O(1)
        """
        if key in self.cache:
            node = self.cache[key]
            # Move to most recently used position
            self._remove(node)
            self._insert_to_tail(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.
        Evict LRU item if over capacity.
        Time Complexity: O(1)
        """
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            # Move to most recently used position
            self._remove(node)
            self._insert_to_tail(node)
        else:
            # Create new node and add to cache
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_to_tail(new_node)
            
            # Evict LRU if over capacity
            if len(self.cache) > self.capacity:
                # LRU node is right after the dummy head
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]


# ==================== TEST ====================
if __name__ == "__main__":
    # Example from problem
    lru_cache = LRUCache(2)
    
    operations = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected = [None, None, 1, None, -1, None, -1, 3, 4]
    
    results = []
    for op, arg, exp in zip(operations, args, expected):
        if op == "put":
            result = lru_cache.put(*arg)
        else:
            result = lru_cache.get(*arg)
        
        results.append(result)
        status = "✓" if result == exp else "✗"
        print(f"{status} {op}({', '.join(map(str, arg))}) = {result} (expected: {exp})")
    
    print(f"\nAll tests passed: {results == expected}")