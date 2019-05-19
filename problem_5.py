import hashlib
import datetime 
import json
import collections
import pprint

timestamp = 'Timestamp: {:%H:%M:%S %Y-%m-%d }'.format(datetime.datetime.now())

class BlockChainNode:
    def __init__(self, data):
    	self.data = data
    	self.next = None
    	self.previous = None

class BlockChain:
	def __init__(self, number, index, timestamp, data, previous_hash):
		self.number = number
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		
		self.hash = self.calc_hash()
		self.hashmap = collections.defaultdict(dict)
		self.head = None
		self.block_chain = []
        
	def __str__(self):  # cite: 1
		node = self.head
		while node:
			self.block_chain.append(str(node.data))
			node = node.next
			return "[" + "<--".join(self.block_chain) + "]"
      
	def calc_hash(self):
		sha = hashlib.sha256()
		sha.update(str(self.timestamp).encode('utf-8') +  # cite: 2 
					str(self.data).encode('utf-8') +
					str(self.previous_hash).encode('utf-8'))
		return sha.hexdigest()
    
	def genesis_block(self, transaction): 
		index = 0
		
		for i,v in enumerate(transaction):
			self.hashmap['Block No.', i] = {}
			self.hashmap['Block No.', i]['Index'] = index
			self.hashmap['Block No.', i]['Timestamp']= transaction['value']
			self.hashmap['Block No.', i]['Data'] = transaction['key']
			self.hashmap['Block No.', i]['SHA256 Hash'] = self.calc_hash()
			self.hashmap['Block No.', i]['Previous Hash'] = self.previous_hash
			
			data = self.hashmap
			# print('hashmap data from genesis: ', data)
			
			node = BlockChainNode(data)
            # print('genesis block node: ', node)
			self.prepend(node) 
        
		return str(self.hashmap), str(self.block_chain)
		
	def get_previous_hash(self, data):
		for i,v in enumerate(data):
			self.previous_hash = data['SHA256 Hash']
			# print('get_prev hash:', self.previous_hash)
			return self.previous_hash
            
	def next_block(self, transaction): 
		for i,v in enumerate(transaction):		# cite: 4
			self.hashmap['Block No.', i] = {}
			self.hashmap['Block No.', i]['Index'] = i
			self.hashmap['Block No.', i]['Timestamp'] = transaction['value']
			self.hashmap['Block No.', i]['Data'] = transaction['key']
			self.hashmap['Block No.', i]['SHA256 Hash'] = self.calc_hash()
			self.hashmap['Block No.', i]['Previous Hash'] = self.get_previous_hash(self.hashmap['Block No.', i-1])
			
			node = BlockChainNode(self.hashmap)
            #print('next_block node: ', node)
			self.append(node) 
		return str(self.hashmap), str(self.block_chain)
	
	def prepend(self, data):  # add first
		if self.head is None:
			self.head = BlockChainNode(data)
			return
        
		node = BlockChainNode(data)
		node.next = self.head
		self.head = node
		return

	def append(self, data):  # add end
		if self.head is None:
			self.head = BlockChainNode(data)
			return
		
		node = BlockChainNode(data)
		while node.next:
			node = node.next
		node.next = BlockChainNode(data)
		
	def search(self, data):
		if self.head is None:
			self.head = BlockChainNode(data)
			return
		node = self.head
		while node:
			if node.data == data:
				return node
			node = node.next
		
		raise ValueError("Data not found in Blockchain")
		
	def remove(self, data):
		if self.head is None:
			self.head = BlockChainNode(data)
			return
			
		node = self.head
		while node:
			if node.data == data:
				node.next = node.next.next
				return
			node = node.next
		raise ValueError("Data not found in Blockchain")
        
pp = pprint.PrettyPrinter(indent=4)
transaction1 = {"key": "01100300400602020040", "value": timestamp }

chain = BlockChain(0,0,0,0,0)
pp.pprint(chain)
chain.genesis_block(transaction1)

transaction2 = {"key": "8890234432jijoiIIIIUUUeyyw8", "value": timestamp }
chain.next_block(transaction2)

transaction3 = {"key": "84939939930020AABBBBBeeiew8", "value": timestamp }
pp.pprint(chain.next_block(transaction3))

transaction4 = {"key": "84432mmfkvm9034534klOIIIIif", "value": timestamp }
pp.pprint(chain.next_block(transaction4))

transaction5 = {"key": "84fds9432jij2439OOIIIEPPPPP", "value": timestamp }
pp.pprint(chain.next_block(transaction5))

transaction6 = {"key": "84ioiowr898922234212321YYYY", "value": timestamp }
pp.pprint(chain.next_block(transaction6))

# Citations:
# 1. https://stackoverflow.com/questions/22416626/python-hashtable-linked-lists-how-to-print-a-list-from-the-hashtable-class
# 2. https://medium.com/@vishnuashok123/building-a-simple-blockchain-using-python-90d27ee50214
# 3. https://stackoverflow.com/questions/41168899/does-python-str-function-call-str-function-of-a-class (__str__)
# 4. https://www.programiz.com/python-programming/nested-dictionary (nested)

