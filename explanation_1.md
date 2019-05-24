------ Overview -------------

For the LRU Cache problem we start by declaring our classes LRU Cache and Node. This sets the structure for our algorithm. An LRU Cache can be solved by utilizing two data structures, a doubly linked list and a hashmap because of the hashmap's O(1) constant time lookup and doubly linked lists O(N) removal and insertion. Both are low in space complexity as well at O(N) for the entire algorithm. The approximate Big O run time efficiency of this solution is calculated below: 

1. get() and set() - O(1)
2. remove() and insert() - O(N) 
3. total = O(N)



------- Code Review --------- 

First we declare our Node class variables including key, value, next and previous and set them to None. Our LRU Cache class variables include our hashmap, capacity, head, tail, head.next and tail.previous. We make sure the head and tail point to each other initially. 

Our algorithm is made up of 4 instance methods or functions, two for our hashmap and two for our doubly linked list. 

Our get method checks if node is in the hashmap, if it is that is called our "Cache Hit!" which we then create a node to hold the value at that key in the hashmap. We "refresh" the cache remove the node, and adding it back and returing the value. If our node is not in the cache that is a "Cache Miss!" and we return -1.

Our set method also checks if node is in hashmap, if it is then we remove the least recently used node, assign a new node to hold that value and we refresh the cache, inserting our new node to the linked list and also adding it to our hashmap. If it is not in our hashmap then we assign a new node and add it to our hashmap. If the length of our hashmap is greater than our cache capacity, then we assign our node to head.next and remove the least recently used node and finally delete that node key from our hashmap.

Our remove and insert functions handle our doubly linked list removal of node and insertion of node. For each case we have to remember to keep pointers to our previous and or next nodes before we point to our new node to insert or delete.