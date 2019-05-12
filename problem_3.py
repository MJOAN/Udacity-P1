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

        for a, b in sorted_key_values:
            c = self.huffman_encoding(a)   # extend binary encoding
            print('encoding_debug1: ', c)
            temp_dict.setdefault(a, []).extend([b, c]) 
            print('temp_dict_debug: ', temp_dict)
        return temp_dict

    
    def build_huffman_tree(self, all_sorted_nodes_dict): 
        
        """
        1. build huffman by assigning a binary code to each letter using shorter codes for the more frequent letters 
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
