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
        return out_string + "end"
    
    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def prepend(self, value):
        if self.head is None: 
            self.head = Node(value)
            return
        
        current = Node(value)   
        current.next = self.head   
        self.head = current
        return
    
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    
    def contains(self, value):
        node = self.head
        
        while node is not None:
            if node.value == value:
                return True
            
            node = node.next
        return False
                
    def union(self, llist_1, llist_2):
        union_set = LinkedList()
        
        head_1 = llist_1.head
        head_2 = llist_2.head
        #print(str(head_1.value), str(head_2.value))
        
        while head_1 is not None: 
            union_set.append(head_1.value)   
            #print('union_set append: ', str(union_set))
            head_1 = head_1.next        

        while head_2 is not None:
            if not union_set.contains(head_2.value):
                union_set.append(head_2.value)
            #print('union_set append: ', str(union_set))
            head_2 = head_2.next

        #print('final union', str(union_set))
        return union_set
   
    def intersection(self, llist_1, llist_2):
        intersection = LinkedList()  #  A ∩ B 
        
        head_1 = llist_1.head
        head_2 = llist_2.head
        
        while head_1 is not None and head_2 is not None:
            if head_1.value == head_2.value:
                intersection.append(head_1.value) 
            
            head_1 = head_1.next 
            head_2 = head_2.next
        
        return intersection
           
        
# Test Case 1
llist_1 = LinkedList()
llist_2 = LinkedList()

element_1 = [24, 5436, 86, 345, 2, 6, 9, 0]
element_2 = [24, 56, 87, 0, 42, 543]

for i in element_1:
    llist_1.append(i)

for i in element_2:
    llist_2.append(i)

print('union one: ', llist_1.union(llist_1,llist_2))
print('intersection one: ', llist_1.intersection(llist_1,llist_2))

# Test Case 2
llist_3 = LinkedList()
llist_4 = LinkedList()

element_3 = [3, 4, 54, 65, 7, 8, 90, 5]
element_4 = [65, 43, 23, 54, 7, 89, 4, 3]

for i in element_3:
    llist_3.append(i)

for i in element_4:
    llist_4.append(i)

print('union two: ', llist_3.union(llist_3,llist_4))
print('intersection two:', llist_3.intersection(llist_3,llist_4))

# Test Case 3
llist_5 = LinkedList()
llist_6 = LinkedList()

element_5 = [23, 56, 587, 6675, 757, 8, 945, 234]
element_6 = [65, 42, 757, 4234, 8, 823, 2424]

for i in element_5:
    llist_5.append(i)

for i in element_6:
    llist_6.append(i)

print('union three: ', llist_5.union(llist_5,llist_6))
print('intersection three:', llist_6.intersection(llist_5,llist_6))


