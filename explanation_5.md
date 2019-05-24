------- Overview ----------

A Blockchain can be created implementing a Linked List data structure as it has similar properties to a "chain" and good time complexity for insertion and deletion. Linked List Nodes can store data as well such as a key value store in a Hash Map. 

Using the append function from our Linked List exercises we check if self.head is null and if it is then set our data to a new LinkedListNode else, set self.head to our data passed in to our append function and traverse our Linked List adding or inserting our new Linked List Node at the end. 

Our data will be stored in a Block class with member variables of timestamp, data, previous hash and hash that will hold new data coming into our Linked List Nodes.

1. create new LinkedList - O(1)
2. assign new block to Block - O(1)
3. append block to block chain - O(N)
4. total = O(N)