from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, data):
        self.list.insert_at_front(data)

    def pop(self):
        return self.list.remove_from_front()
