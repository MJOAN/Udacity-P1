import collections

class DoubleNode: 
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache:    
    def __init__(self, capacity):
        self.hashmap = collections.defaultdict()
        self.capacity = 5
        self.head = DoubleNode(0,0)
        self.tail = DoubleNode(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head
                  
    def get(self, key):
        if key not in self.hashmap:
            return -1
                
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._insert(node)
            return node.value
        
    def set(self, key, value):
        if key in self.hashmap:
            self._remove(self.hashmap[key])
            node = DoubleNode(key, value)
            self._insert(node)
            self.hashmap[key] = node
        else: 
            node = DoubleNode(key, value) 
            self.hashmap[key] = node
        
            if len(self.hashmap) > self.capacity:
                node = self.head.next 
                self._remove(node)
                del self.hashmap[node.key] 
                
    def _remove(self, node): # cite: 1        
        if self.head is None or node is None:
            return 
        
        if self.head == node:
            self.head = node.next
            
        if node.next is not None:
            node.next.previous = node.previous
        
        if node.previous is not None:
            node.previous.next = node.next
            
    def _insert(self, node):
        node.next = self.head
        node.previous = None

        if self.head is not None:
            self.head.previous = node
        self.head = node



# Test Case 1
our_cache = LRU_Cache(5)
print('test_cache', our_cache)
our_cache.set(1, 3)
our_cache.set(2, 4)   
print('test_1_cache', our_cache)
print('test_1_get', our_cache.get(1)) # returns 1
print('test_1_get', our_cache.get(2)) # returns 2
print('test_1_get', our_cache.get(3)) # return -1

# Test Case 2
our_cache.set(3, 5)
print('test_2_cache', our_cache)
print('test_2_get', our_cache.get(2)) # returns 4
our_cache.set(4, 5)
print('test_2_cache', our_cache)

# Test Case 3
print('test_3_cache', our_cache)
print('test_3_get', our_cache.get(1)) # returns 3
print('test_3_get', our_cache.get(3)) # returns 5
our_cache.set(3, 6)
print('test_3_cache', our_cache) 

# citations: 
# 1. https://www.geeksforgeeks.org/delete-a-node-in-a-doubly-linked-list/ 