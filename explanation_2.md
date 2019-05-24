------ Overview -------------

The os.walk() method from the os module was used to traverse the root directory, subsequent directories and the files within those directories. From there a second for loop nested would iterate over the files and an if statement using a built in string function .endswith() to locate the suffix. 

1. for loop = O(N) * 2
2. if statement = O(1)
3. total = O(N^2) * O(1)
4. result = O(N^2)