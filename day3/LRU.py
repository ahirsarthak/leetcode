

class Node:
    def __init__(self, key, val) -> None:
        # making a node class that we will use
        self.key, self.val = key, val
        # pointers
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # map key to node
        self.cache = {}
        # dummy nodes

        self.left, self.right = Node(0, 0), Node(0, 0)

        # to eb connected to each other
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = prev, nxt

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # to update to most recent
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove fromm the list and delete the LRU from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
