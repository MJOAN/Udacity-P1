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

    def __eq__(self, node):  # enables heappop and heappush methods when not using tuples
        if self is node:
            return True
        elif type(self) != type(node):
            return False
        else:
            return self.value == node.value

    def __lt__(self, node):  # enables to compare "frequencies" with tree nodes
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
        """
        1. convert string to hashmap with keys as string characters and frequency as values 
        2. build and sort a list of tuples from lowest to highest frequencies
        3. convert tuples list to dictionary of key values
        4. call build tree function with dictionary key values
        """
        codes = dict()
        for char in string:
            if char not in codes:
                codes[char] = 1
            else:
                codes[char] += 1
        
        #print('codes hashmap: ', codes)
        return self.build_huffman_tree(codes)
    
    def build_huffman_tree(self, codes):     
        """
        1. build huffman by assigning a binary code to each letter using shorter codes for the more frequent letters 
        2. trim the Huffman Tree (remove the frequencies from the previously built tree)

        """

        Q = [] # Q is representing a list of frequencies 
        
        for key, value in codes.items():  
            # looping until PQ only has one element             
            node = HuffmanNode(key, value)
            heappush(Q, (node))
            #print('node', node)
            
        while len(Q) != 1:  # while length of list frequencies != 1 
            priority_queue = HuffmanNode()
            priority_queue.left = heappop(Q) 
            priority_queue.right = heappop(Q)
            priority_queue.value = priority_queue.left.value + priority_queue.right.value  # merge the two freq's 
            heappush(Q, (priority_queue))  
        
        self.depth_first_search(priority_queue, "")         
        
        #print('tree: ', str(priority_queue))
        return priority_queue  # return parent node


    def depth_first_search(self, node, path):
        """
        # use a dfs search for leaf node to a dict mapping char to huffman code/path
        1. base case checks for child nodes --> for a leaf 
        2. recursive case checks for the char & then we obtain the path to get there 
        store that in dictionary as --> node.key
        """
        if node.get_left_child() is None and node.get_right_child() is None:
            self.huffman_code_map[node.key] = path
            #print('huffcode_map:', self.huffman_code_map)
        else: 
            self.depth_first_search(node.left, path + "0")
            self.depth_first_search(node.right, path + "1")


    def huffman_encoding(self, data):    # cite: 4 
        encoded_data = ""        
        for char in data:     
            encoded_data += self.huffman_code_map[char]  
        return encoded_data

    def huffman_decoding(self, encoded_data, tree):    # cite: 4 
        decoded_data = ""
        print('tree', tree)
        root = tree
        node = root
        
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

    print('tree.huff.encoding: ', tree_one.huffman_encoding(a_great_sentence))
    print('tree.huff.decoding: ', tree_one.huffman_decoding(a_great_sentence, tree_one))


    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = tree_one.huffman_encoding(a_great_sentence)
    print('encoded_data, tree: ', encoded_data, tree_one)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = tree_one.huffman_decoding(encoded_data, tree_one)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 2 
    tree_two = HuffmanBinaryTree()
    a_great_sentence = "I love computer science so much"

    tree_two.relevant_frequencies(a_great_sentence)

    print('tree.huff.encoding: ', tree_two.huffman_encoding(a_great_sentence))
    print('tree.huff.decoding: ', tree_two.huffman_decoding(a_great_sentence, tree_two))

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = tree_two.huffman_encoding(a_great_sentence)
    print('encoded_data, tree: ', encoded_data, tree_two)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = tree_two.huffman_decoding(encoded_data, tree_two)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Citations: 
# 1. https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# 2. https://stackoverflow.com/questions/39495924/how-to-convert-python-list-of-tuples-into-tree
# 3. https://www.geeksforgeeks.org/python-convert-list-tuples-dictionary/
# 4. https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
# 5. https://stackoverflow.com/questions/51425638/how-to-write-huffman-coding-to-a-file-using-python
# 6. https://svn.python.org/projects/python/trunk/Lib/heapq.py heapq libary