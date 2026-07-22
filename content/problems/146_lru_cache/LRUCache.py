class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.left, self.right = Node(0, -1), Node(0, -1)
        self.left.next, self.right.prev = self.right, self.left
        self.cache: dict[int, Node] = {}

    def remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print('cache.get(1)', cache.get(1))
    cache.put(3, 3)
    print('cache.get(2)', cache.get(2))


if __name__ == '__main__':
    main()
