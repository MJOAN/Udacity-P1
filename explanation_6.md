------- Overview ----------

Our Linked List union and intersection class methods from our Linked List class would both be O(N*M) time complexity because we are iterating over two different data sets in order to find our common elements. Our append method in both cases is O(N). Our space complexity also O(N) because we are allocating space for the new Linked List of size N.

Union: 
1. assign two new variables - O(1) * 2
2. two while loops - O(N), O(M)
3. append method - O(N)
4. if statement - O(1)
5. total = O(M + N) 

Intersection: 
1. assign two new variables - O(1) * 2
2. while loop over two data sets - O(N), O(M)
3. append method - O(N)
4. if statement - O(1)
4. total = O(N + M) 