import sys

class HuffmanNode(): 
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
    
    def set_value(value):
        self.value = value
                
    def get_value(value):
        return self.value

    def get_left_child(self):
        return self.left
        
    def get_right_child(self):
        return self.right
        
    def set_left_child(self, node):
        self.left = node
        
    def set_right_child(self, node):
        self.right = node
    
    def has_left_child(self):
        return self.left != None
        
    def has_right_child(self):
        return self.right != None
        
class HuffmanBinaryTree(object):
    def __init__(self):
        self.root = None

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
        
        print('codes hashmap: ', codes)
        
        sorted_key_values = sorted(codes.items(), key=lambda kv: kv[1])  # cite: 1
        all_sorted_nodes_dict = self.convert_tuple_dict(sorted_key_values)
        print('all_sorted_debug1: ', all_sorted_nodes_dict)
        
        self.build_huffman_tree(all_sorted_nodes_dict)
    
    def convert_tuple_dict(self, sorted_key_values): # cite: 3
        """
        1. create dict with key as char and value as frequency
        2. values are setup as an list so I can add binary code later
        """
        temp_dict = dict()

        for a, b in sorted_key_values:   # iterate over tuple key, values 
            c = self.huffman_encoding(a)    # get binary encodings for each key -> char  
            print('encoding_debug1: ', c)
            temp_dict.setdefault(a, []).extend([b, c]) # extend values and binary encoding 
            print('temp_dict_debug: ', temp_dict) 
        return temp_dict
    
    def build_huffman_tree(self, all_sorted_nodes_dict):        
        """
        1. build huffman assign binary code to each char w/ shorter codes for the more frequent chars 
        2. trim the Huffman Tree (remove the frequencies from the previously built tree)

        """
        node = self.get_root()

        for key, value in all_sorted_nodes_dict.items():   # cite: 2
            huffman_node = HuffmanNode(key, value)    
            print('key value iterate over dict: ', key, value)
            
            if node is not None:
                if node.value < huffman_node.value:
                    if node.has_left_child():
                        node = node.get_left_child()
                    else:
                        node.set_left_child(huffman_node)
                        break
                else:
                    if node.has_right_child():
                        node = node.get_right_child()
                    else:
                        node.set_right_child(huffman_node)
                        break
            else:
                node = huffman_node
                print('huffman_node_debug1: ', node)
        
    def huffman_encoding(self, data):    # cite: 4 
        return bin(int.from_bytes(data.encode(), 'big'))

    def huffman_decoding(data,tree):    # cite: 4
        n = int(data, 2)
        n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Citations: 
# 1. https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# 2. https://stackoverflow.com/questions/39495924/how-to-convert-python-list-of-tuples-into-tree
# 3. https://www.geeksforgeeks.org/python-convert-list-tuples-dictionary/
# 4. https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
# 5. https://stackoverflow.com/questions/51425638/how-to-write-huffman-coding-to-a-file-using-python



##################OPTION 2: INCORPORATING A PRIORITY QUEUE WITH BINARY TREE########################################

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
        
        
    def __eq__(self, node): # enables us to avoid tuple and == and < with heappush and heappop methods 
        if self is node:
            return True
        elif type(self) != type(node):
            return False
        else:
            return self.value == node.value

    def __lt__(self, node): # less than how we are going to compare frequencies
        return self.value < node.value  # self has a node 
    
    def set_value(value):
        self.value = value
                
    def get_value(value):
        return self.value

    def get_left_child(self):
        return self.left
        
    def get_right_child(self):
        return self.right
        
    def set_left_child(self, node):
        self.left = node
        
    def set_right_child(self, node):
        self.right = node
    
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
        
        print('codes hashmap: ', codes)
        
        return self.build_huffman_tree(codes)
    
    def build_huffman_tree(self, codes): 
        
        """
        1. build huffman by assigning a binary code to each letter using shorter codes for the more frequent letters 
        2. trim the Huffman Tree (remove the frequencies from the previously built tree)

        """
        #  node = self.get_root()
        Q = [] # representing a list of frequencies 
        
        for key, value in codes.items():  
            # looping until PQ only has one element             
            node = HuffmanNode(key, value)
            heappush(Q, (node))
            print('node', node)
            
        while len(Q) != 1:  # while frequencies are not = 1 
            priority_queue = HuffmanNode()
            priority_queue.left = heappop(Q) 
            priority_queue.right = heappop(Q)
            priority_queue.value = priority_queue.left.value + priority_queue.right.value  # merge the two freq's 
            heappush(Q, (priority_queue))  
        
        # dfs search for leaf node to a dict mapping char to huffman code/path
        self.depth_first_search(priority_queue, "")         
        
        print('tree: ', str(priority_queue))
        return priority_queue  # return parent node

        
        
    def depth_first_search(self, node, path):


        # base case check for child nodes -- for a leaf 
        if node.get_left_child() is None and node.get_right_child() is None:
            self.huffman_code_map[node.key] = path
            print('huffcode_map:', self.huffman_code_map)

        # recursive case checking for the char and then we 
        # obtain the path to get there and store that in dictionary # node.key

        else: 
            self.depth_first_search(node.left, path + "0")
            self.depth_first_search(node.right, path + "1")



    def huffman_encoding(self, data):    # cite: 4 
        encoded_data = ""
        
        for char in data:     # each char in data
            encoded_data += self.huffman_code_map[char]  # lookup code for char a, b, c, etc... 
        
        return encoded_data


    def huffman_decoding(self, encoded_data, tree):    # cite: 4 
        decoded_data = ""
        
        for byte in encoded_data: # for each encoded byte in input stream 
            node = HuffmanNode()
            while node.has_left_child() is not None and node.has_right_child() is not None:
                if encoded_data[0] == '0':
                    node = node.get_left_child()
                else:
                    node = node.get_right_child()
                    decoded_data += byte
            return decoded_data
        
        



if __name__ == "__main__": # checks to see if file is being run as a script instead of being run as a module 
    # if not then it will be name of inputed module 

    tree = HuffmanBinaryTree()
    print(tree, 'tree')
    tree.relevant_frequencies(a_great_sentence)
    print('tree.huff.encoding: ', tree.huffman_encoding(a_great_sentence))
    print('tree.huff.decoding: ', tree.huffman_decoding(a_great_sentence, tree))

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = tree.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = tree.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    

    
tree = HuffmanBinaryTree()
# a_great_sentence = "The bird is the word"
tree.relevant_frequencies(a_great_sentence)
tree.huffman_encoding(a_great_sentence)

# leaf node is char 
# if you hit a 0 go 
