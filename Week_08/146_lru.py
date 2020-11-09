#version 1 dict + double linked list
class DLinkedNode:

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                removed = self.removeTail()
                self.cache.pop(removed.key)
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
                
    
    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
    
    def addToHead(self, node):
        next = self.head.next
        node.prev = self.head
        node.next = next
        self.head.next = node
        next.prev = node 

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

#version 2: OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.cache.popitem(last = False)
        self.cache[key] = value

