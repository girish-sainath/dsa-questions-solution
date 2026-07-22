import collections


class ListNode:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self) -> int:
        return len(self.map)

    def push_right(self, val) -> None:
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val) -> None:
        if val in self.map:
            node = self.map[val]
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
            del self.map[val]

    def pop_left(self) -> int:
        res = self.left.next.val
        self.pop(res)
        return res

    def update(self, val):
        self.pop(val)
        self.push_right(val)


class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.lfu_count = 0
        self.cache = {}
        self.count_map = collections.defaultdict(int)
        self.list_map = collections.defaultdict(LinkedList)

    def counter(self, key: int) -> None:
        count = self.count_map[key]
        self.count_map[key] += 1
        self.list_map[count].pop(key)
        self.list_map[count + 1].push_right(key)

        if count == self.lfu_count and self.list_map[count].length() == 0:
            self.lfu_count += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -2
        self.counter(key)
        return self.cache[key]

    def put(self, key: int, val: int) -> int:
        if self.cap == 0:
            return -1

        if key not in self.cache and len(self.cache) == self.cap:
            res = self.list_map[self.lfu_count].pop_left()
            del self.cache[res]
            del self.count_map[res]

        self.cache[key] = val
        self.counter(key)
        self.lfu_count = max(self.lfu_count, self.count_map[key])
        return -2


def main():
    cache = LFUCache(2)
    print(-2)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))
    print(cache.put(3, 3))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.put(4, 4))
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))


if __name__ == '__main__':
    main()
