class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.cache = {}
        self.left = self.right = Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left

    # remove the item from the list
    def _remove(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # insert at the end of the list
    def _insert(self, node: Node) -> None:
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, val)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.cap:
            node = self.left.next
            del self.cache[node.key]
            self._remove(node)


def main():
    cache = LRUCache(2)
    print(cache.get(1))  # -1
    cache.put(3, 3)
    cache.put(2, 2)
    print(cache.get(3))  # 3
    cache.put(1, 1)
    print(cache.get(2))  # -1


if __name__ == '__main__':
    main()
