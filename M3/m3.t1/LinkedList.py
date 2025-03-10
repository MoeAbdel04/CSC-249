class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        """Add a node to the end of the linked list."""
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def prepend(self, new_node):
        """Add a node to the beginning of the linked list."""
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_node):
        """Insert a new node after a given node."""
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node

    def remove_after(self, prev_node):
        """Remove the node after the given node."""
        if prev_node is None:
            if self.head is not None:
                self.head = self.head.next
        elif prev_node.next is not None:
            prev_node.next = prev_node.next.next

    def print_list(self):
        """Print the linked list elements."""
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()
