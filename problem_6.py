class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def prepend(self, value):
        if self.head is None: 
            self.head = Node(value)
            return
        
        current = Node(value)   
        current.next = self.head   
        self.head = current
        return

    def union(self, llist_1, llist_2):
        union_set = LinkedList()
                
        head_1 = Node(llist_1)
        head_2 = Node(llist_2)
        
        while head_1.next is not None: 
            union_set.append(head_1.value)   
            head_1 = head_1.next        

        while head_2.next is not None:
            union_set.append(head_2.value)
            head_2 = head_2.next

        return union_set
   
    def intersection(self, llist_1, llist_2):
        intersection = LinkedList()  #  A ∩ B 
        
        head_1 = Node(llist_1)
        head_2 = Node(llist_2)
        
        while head_1.next is not None and head_2.next is not None:
            if head_1.value == head_2.value:
                intersection.append(head_1.value)   
            
            head_1 = head_1.next 
            head_2 = head_2.next
            
        return intersection

# Test case 1
llist_1 = LinkedList()
llist_2 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    llist_1.append(i)

for i in element_2:
    llist_2.append(i)

print('union', llist_1.union(llist_1,llist_2))
print('inter', llist_1.intersection(llist_1,llist_2))

# Test case 2
llist_3 = LinkedList()
llist_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    llist_3.append(i)

for i in element_2:
    llist_4.append(i)

print(llist_3.union(llist_3,llist_4))
print(llist_4.intersection(llist_3,llist_4))
