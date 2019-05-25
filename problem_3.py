import sys
from heapq import * 

class HuffmanNode(): 
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):     
        if self.left or self.right:  
            return "(" + str(self.left) + " " + str(self.right) + ")"
        else: 
            return str(self.key)

    def __eq__(self, node):  
        # enables heappop and heappush methods when not using tuples
        if self is node:
            return True
        elif type(self) != type(node):
            return False
        else:
            return self.value == node.value

    def __lt__(self, node):  
        # enables to compare "frequencies" with tree nodes
        return self.value < node.value
    
    def get_left_child(self):
        return self.left
        
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
        
    def has_right_child(self):
        return self.right != None
        
class HuffmanBinaryTree(object):
    def __init__(self):
        self.root = None
        self.huffman_code_map = dict()

    def get_root(self):
        return self.root
        
    def relevant_frequencies(self, string): 
        codes = dict()
        
        if string is None or string == "" or not string:
            return '0'

        for char in string:
            if char not in codes:
                codes[char] = 1
            else:
                codes[char] += 1
        
        #print('codes hashmap: ', codes)
        return self.build_huffman_tree(codes)
    
    def build_huffman_tree(self, codes):     
        Q = [] 
        # Q is representing a list of frequencies 

        for key, value in codes.items():  
            # looping until PQ only has one element             
            node = HuffmanNode(key, value)
            heappush(Q, (node))
            #print('node', node)
            
        while len(Q) != 1:  
            # while length of list frequencies != 1 
            priority_queue = HuffmanNode()
            priority_queue.left = heappop(Q) 
            priority_queue.right = heappop(Q)
            priority_queue.value = priority_queue.left.value + priority_queue.right.value  # merge the two freq's 
            heappush(Q, (priority_queue))  
        
        self.depth_first_search(priority_queue, "")         
        return priority_queue  # return parent node


    def depth_first_search(self, node, path):
        if node.get_left_child() is None and node.get_right_child() is None:
            self.huffman_code_map[node.key] = path
        else: 
            self.depth_first_search(node.left, path + "0")
            self.depth_first_search(node.right, path + "1")

    def huffman_encoding(self, data):    # cite: 4 
        encoded_data = ""
        if data is None or data == "" or not data:
            return '0'  

        for char in data:     
            encoded_data += self.huffman_code_map[char]  
        return encoded_data

    def huffman_decoding(self, encoded_data, tree):    # cite: 4 
        decoded_data = ""
        node = root = tree
        
        for i, v in enumerate(encoded_data): 
            #print('node_decoding, i:', i) 
            new_node = HuffmanNode(node)
            
            if encoded_data[i] == '0':
                node = new_node.get_left_child()
                #print('node_decoding:', node)
            else:
                node = new_node.get_right_child()
                #print('node_decoding:', node)
                
            if new_node.has_left_child() is not None and new_node.has_right_child() is not None:
                decoded_data += v
                #print('decoded_data: ', v, decoded_data)
                node = root
        
        return decoded_data+'\0'
        
if __name__ == "__main__": 

    # Test Case 1
    tree_one = HuffmanBinaryTree()
    a_great_sentence = "Happy days are ahead not to mention presently"

    tree_one.relevant_frequencies(a_great_sentence)

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # 94
    print ("The content of the data is: {}\n".format(a_great_sentence)) # Happy days are ahead not to mention presently

    encoded_data = tree_one.huffman_encoding(a_great_sentence) 

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 48
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 00110011101010101000110100110111000111101100110010010110011111111010011100111101110101100011000010111100011101011100001111101011111011010100010010111100101110000100101000

    decoded_data = tree_one.huffman_decoding(encoded_data, tree_one)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 220
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # 00110011101010101000110100110111000111101100110010010110011111111010011100111101110101100011000010111100011101011100001111101011111011010100010010111100101110000100101000

    # Test Case 2 
    tree_two = HuffmanBinaryTree()
    a_great_sentence = "I love computer science so much"

    tree_two.relevant_frequencies(a_great_sentence)

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # 80
    print ("The content of the data is: {}\n".format(a_great_sentence)) # I love computer science so much

    encoded_data = tree_two.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 40
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 00010111000110010111110011111000101101011101011011010001110111010011010100100101011101001110100001111011001011100000

    decoded_data = tree_two.huffman_decoding(encoded_data, tree_two)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 166
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # 00010111000110010111110011111000101101011101011011010001110111010011010100100101011101001110100001111011001011100000

    # Test Case 3 - Empty 
    tree_three = HuffmanBinaryTree()
    a_great_sentence = ""

    tree_three.relevant_frequencies(a_great_sentence)

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # 49
    print ("The content of the data is: {}\n".format(a_great_sentence)) # empty

    encoded_data = tree_three.huffman_encoding(a_great_sentence) 

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 24
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 0

    decoded_data = tree_three.huffman_decoding(encoded_data, tree_three)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 51
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # 0

# Citations: 
# 1. https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# 2. https://stackoverflow.com/questions/39495924/how-to-convert-python-list-of-tuples-into-tree
# 3. https://www.geeksforgeeks.org/python-convert-list-tuples-dictionary/
# 4. https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
# 5. https://stackoverflow.com/questions/51425638/how-to-write-huffman-coding-to-a-file-using-python
# 6. https://svn.python.org/projects/python/trunk/Lib/heapq.py heapq libary