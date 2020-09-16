#https://leetcode.com/problems/lru-cache/

class DuleNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        
class LRUCache:
    # hash + double pointers

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DuleNode()
        self.tail = DuleNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.movetoHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DuleNode(key, value)
            self.cache[key] = node
            self.addtoHead(node)
            self.size += 1
            if self.size > self.capacity:
                deleted = self.removeTail()
                self.cache.pop(deleted.key)
                self.size -= 1
                
        else:
            node = self.cache[key]
            node.val = value
            self.movetoHead(node)
            
            
        
    def addtoHead(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
    
    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        
    def movetoHead(self, node):
        self.removeNode(node)
        self.addtoHead(node)
        
    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
