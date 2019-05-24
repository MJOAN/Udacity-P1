import hashlib
import datetime

timestamp = 'Timestamp: {:%H:%M:%S %Y-%m-%d }'.format(datetime.datetime.now())

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):  
        if self.head is None:
            self.head = LinkedListNode(data)
            return
        
        else: 
            node = self.head 
            while node.next:
                node = node.next
            node.next = LinkedListNode(data)

    def __str__(self):  # cite: 1  
        node = self.head
        block_chain = [] 
        while node:
            block_chain.append(str(node.data))
            node = node.next
        return "[" + "<--".join(block_chain) + "]"
    
class Block: 
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def __str__(self):  # cite: 1  
        return "[" + "timestamp: "  + self.timestamp + "data: " + self.data + "prev_hash: " + self.previous_hash + "hash: " + self.hash + "]"
              
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +  # cite: 2 
                      str(self.data).encode('utf-8') +
                      str(self.previous_hash).encode('utf-8'))   
        return sha.hexdigest()
        

# Test Case 1
block_chain_one = LinkedList()
previous_hash = ""

blocka = Block(timestamp,"01100300400602224f342220040", previous_hash)
blockb = Block(timestamp,"84939939930020AABBBBBeeiew8", blocka.hash)
blockc = Block(timestamp,"342352543253urtruuewrw34234", blockb.hash)

block_chain_one.append(blocka) 
block_chain_one.append(blockb)
block_chain_one.append(blockc)
print('block_chain_one: ', str(block_chain_one))

# Test Case 2
block_chain_two = LinkedList()

blockd = Block(timestamp,"2342525252k-23423423", previous_hash)
blocke = Block(timestamp,"849399234-f345354ew8", blockd.hash)
blockf = Block(timestamp,"3423525432-rt9876784", blocke.hash)

block_chain_two.append(blockd) 
block_chain_two.append(blocke)
block_chain_two.append(blockf)
print('block_chain_two: ', str(block_chain_two))


# Citations:
# 1. https://stackoverflow.com/questions/22416626/python-hashtable-linked-lists-how-to-print-a-list-from-the-hashtable-class
# 2. https://medium.com/@vishnuashok123/building-a-simple-blockchain-using-python-90d27ee50214
# 3. https://stackoverflow.com/questions/41168899/does-python-str-function-call-str-function-of-a-class (__str__)
# 4. https://www.programiz.com/python-programming/nested-dictionary (nested)