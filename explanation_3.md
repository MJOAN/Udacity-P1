------- Overview ----------

The Huffman Coding algorithm is utilizing a Binary Tree, a Queue, a MinHeap, and a Hashmap. Breaking down this problem into sub problems is really the only way to accomplish the goal here because of the complexity in creating the tree itself and finally retrieving the leafs with ordered paths and thus, encoded data. The time and space complexity is approximated below which I believe was the most efficient given our constraints. 

1. Build Map - O(N)
2. Binary Tree Insertion/Deletion - O(N) 
3. Queue - O(N)
4. Heap Push/Pop - O(log N)
5. DFS Adjacency List - O(V+E)
6. Encoded - O(N)
7. Decoded - O(M) + O(1) * 2
8. Result: O(N) * 4 + O(M) + O(V+E) + O(log N) = O(N Log N)


------- Code Review ----------

In this algorithm we start importing sys and heapq. Reading through documentation using the built in methods of heapq was a quicker way to build the binary tree with frequencies than implementing a full priority queue. The next steps are creating the Node and Binary Tree classes since we know these two components are the main vehicles of our program allowing us to iterate and traverse our tree. I learned an important point of including __str__, __lt__ and __eq__ dunder methods to our Node class so that we could work with operators within our tree values while using heapq and also to be able to print out our objects. I utilized basic helper instance methods like get_left_child() and set_left_child() for more efficiency. 

Our Binary Tree class included a hashmap and a basic get_root instance method. This function starts the process of mapping our string to our dictionary and includes a frequency value for each number of times that character appears in our string. I included the build tree helper function to start builing our tree with these values collecting in our hashmap.

A basic Binary Search Tree implementation would not be useful here as I learned because this tree needs to be built in a certain way to allow for lowest frequencies on the bottom nodes with higher frequencies on the top, unlike the way a BST which has an invariant of nodes on left are less than the parent and vice versa. The intent with Huffman is to use fewer bytes or codes for more frequent characters.

Here, we have to add the values from the two lowest frequencies and then merge the two nodes into one parent node that will include a total of both frequencies. The only option here was to use a Queue data structure to handle the merging and insertion of nodes to the tree. 

By assigning a list to which we can "push" or "pop" values while using the heapq module was going to work well. In the `build_huffman_tree` we iterate over the `codes.items` key and values assigning our new `HuffmanNode` with the key and value and "pushing" our new node to the Queue list. While the length of this list or Queue is not one we assign a Priority Queue as a new `HuffmanNode` and `pop` the left and right child nodes adding their values and pushing that total value as a new node to the Queue. 

Finally a depth first search was required in order to search for each node's children as we traverse the tree to add our "codes" or binary code concept. In this DFS we want to make sure that the node is not a leaf but, rather it has a left and right child. When that is true, we run DFS recursively once, passing in our left node, and concatanating our "path" + "0" then second time, passing in our right child concatanating our "path" + "0". This forms our "binary code"! 

Finally our Huffman encoding function simply takes in the data from our tree which are our dictionary values (assigned as huffman_code_map), and concatanates these values! 

Lastly, our Huffman decoding includes a reference to our tree and assigning that as our root node and iterates over our encoded data, assigning a new HuffmanNode passing in our root and if encoded data is "0" then we get the node's left child and assign that to a new node else assign the node's right child. If left or right child nodes are null then we concatanate the value from our iteration to a new string called decoded data and return that when iteration ends!




