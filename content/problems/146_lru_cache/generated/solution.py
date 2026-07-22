class Node:
    """Doubly linked list node"""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache implementation using HashMap + Doubly Linked List
    
    Structure:
    - head (dummy) <-> [MRU] <-> ... <-> [LRU] <-> tail (dummy)
    - HashMap: key -> Node
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Initialize dummy head and tail nodes
        # head.next = Most Recently Used
        # tail.prev = Least Recently Used
        self.head = Node()  # dummy head
        self.tail = Node()  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        """Remove a node from the doubly linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _insert_at_front(self, node: Node) -> None:
        """Insert a node right after the dummy head (most recently used position)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        """
        Return value if key exists, else -1
        Move accessed node to front (most recently used)
        Time: O(1)
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Move to front (mark as most recently used)
        self._remove(node)
        self._insert_at_front(node)
        
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair
        If capacity exceeded, evict least recently used (tail.prev)
        Time: O(1)
        """
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            # Move to front (mark as most recently used)
            self._remove(node)
            self._insert_at_front(node)
        else:
            # Create new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_at_front(new_node)
            
            # Check capacity and evict LRU if needed
            if len(self.cache) > self.capacity:
                # Evict the least recently used node (just before dummy tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]


# ============================================================
# Testing
# ============================================================
def run_test(operations: list, arguments: list) -> list:
    """Run a sequence of operations and return results"""
    results = []
    lru_cache = None
    
    for op, args in zip(operations, arguments):
        if op == "LRUCache":
            lru_cache = LRUCache(args[0])
            results.append(None)
        elif op == "get":
            results.append(lru_cache.get(args[0]))
        elif op == "put":
            lru_cache.put(args[0], args[1])
            results.append(None)
    
    return results


# Example Test Case
operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
expected = [None, None, None, 1, None, -1, None, -1, 3, 4]

results = run_test(operations, arguments)

print("Operations:", operations)
print("Arguments: ", arguments)
print("Expected:  ", expected)
print("Got:       ", results)
print("Pass:", results == expected)