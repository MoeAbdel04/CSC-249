from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, data):
        self.list.insert_at_end(data)

    def dequeue(self):
        return self.list.remove_from_front()
