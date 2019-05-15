import collections

class DoubleNode: 
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
    

class LRU_Cache:    
    def __init__(self, capacity):
        """
        declare the hashmap in this class with cap, head and tail
        also, include relation of head.next and tail.prev so they
        point to each other initially 
        """
        self.hashmap = collections.defaultdict()
        self.capacity = 5
        self.head = DoubleNode(0,0)
        self.tail = DoubleNode(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head
    
                
    def get(self, key):
        """
        put()/get() we use constant time O(1) lookups
        check if node is in hashmap 
        1. if key in hashmap ==> a cache_hit!
        create node to hold that value at that key
        2. node = self.hashmap[key]
        now refresh so remove node, add back and return value
        3. remove(node), add(node), return node value  
        else if not in cache ==> a cache_miss!
        4. return -1
        """
        if key not in self.hashmap:
            return -1
        
        print('test_map', key, self.hashmap)
        
        if key in self.hashmap:
            print('test_map_inside iteration: ', self.hashmap[key])
            node = self.hashmap[key]
            print('get method node: ', node)
            self._remove(node)
            self._insert(node)
            print('get_node', node.value)
            return node.value
        

    def set(self, key, value):
        """
        put()/get() we use constant time O(1) lookups
        check if node is in hashmap 
        1. if key in hashmap
        assign node to hold that value at that key
        2. node = self.hashmap[key]
        now refresh so remove node and add back
        3. remove(node), add(node) and set that node as value to hashmap
        check hashmap length > LRU capacity
        """
        print('test_key_value: ', key, value)
        print('test_hashmap before iteration: ', self.hashmap)
        
        if key not in self.hashmap:
            # node = DoubleNode(key, value)
            node = self.hashmap[key]
            print('key_not_in_hashmap: ', node)
        
        if key in self.hashmap:
            self._remove(self.hashmap[key])
            print('test_map', self.hashmap)
            node = DoubleNode(key, value)
            print('node:', node)
            self._insert(node)
            self.hashmap[key] = node
            print('from set test_hashmap: ', self.hashmap)
            

            
            """
            if hashmap exceeds capacity remove LRU node aka oldest item
            we keep the head and tail as pointers so the LRU is the tail
            while head is MRU most recently used 
            also, evict the node from doubly linked list and from hashmap as well

            """
        if len(self.hashmap) > self.capacity:
            node = self.head.next # or is it --> self.tail? 
            print('len > cap_node:', node)
            self._remove(node)
            del self.hashmap[node.key]
            """
            else we set the value if the key is not present in the hashmap
            create a new node and insert it at head of doubly linked list
            the also add to hashmap, storing new node as value

            """     
                
    def _remove(self, node):
        """
        remove()/insert() handle our doubly linked list functions:
        declare prev and next from our node we need to remove
        1. prev = node.prev, next = node.next
        then connect these together "over" our node 
        2. prev.next = next, next.prev = prev
        """
        print('_remove_node:', node)
        p = node.previous
        n = node.next
        p.next = n
        n.previous = p
    
    
    def _insert(self, node):
        """
        remove()/insert() handle our doubly linked list functions:
        find prev from tail 
        1. prev = self.tail.prev
        set prev.next to node we want to add and set tail.prev to node too
        2. prev.next = node, self.tail.prev = node
        finish up with connecting our node to prev and next
        3. node.prev = prev, node.next = self.tail 
        """    
        print('_insert_node:', node)
        p = self.tail.previous
        p.next = node
        self.tail.prev = node
        
        node.previous = p
        node.next = self.tail
    
    
our_cache = LRU_Cache(5)
print('test_cache', our_cache)
our_cache.set(1, 3)
our_cache.set(2, 4)    # returns 1
print('test_cache', our_cache)
print('test_get', our_cache.get(1)) # # returns 1
print('test_get', our_cache.get(2)) # returns 2
print('test_get', our_cache.get(3))  # return -1
our_cache.set(3, 5)
print('test_cache', our_cache)
print('test_get', our_cache.get(2))
our_cache.set(4, 5)
print('test_cache', our_cache)
print('test_get', our_cache.get(1))
print('test_get', our_cache.get(3))
our_cache.set(3, 5)
print('test_cache', our_cache)