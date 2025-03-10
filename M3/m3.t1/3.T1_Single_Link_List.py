from Node import Node
from LinkedList import LinkedList

num_list = LinkedList()

node_a = Node(10)
node_b = Node(55)
node_c = Node(77)
node_d = Node(88)
node_e = Node(33)
node_f = Node(22)

num_list.append(node_b)   # Add 55
num_list.append(node_c)   # Add 77, make the tail
num_list.append(node_e)   # Add 33, make the tail

num_list.prepend(node_a)  # Add 10, make the head

num_list.insert_after(node_c, node_d)  # Insert 88 after 77
num_list.insert_after(node_e, node_f)  # Insert 22 after tail (33)

# Output list
print('List after adding nodes:', end=' ')
node = num_list.head
while node is not None:
    print(node.data, end=' ')
    node = node.next
print()

num_list.remove_after(node_e)   # Remove the tail (22)
num_list.remove_after(None)     # Remove the head (10)

# Output final list
print('List after removing nodes:', end=' ')
node = num_list.head
while node is not None:
    print(node.data, end=' ')
    node = node.next
print()
