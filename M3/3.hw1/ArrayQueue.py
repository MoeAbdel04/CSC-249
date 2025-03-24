class ArrayQueue:
    def __init__(self, max_length=None):
        self.queue = []
        self.max_length = max_length
    
    def enqueue(self, item):
        if self.max_length is not None and len(self.queue) >= self.max_length:
            raise Exception("Queue is full")
        self.queue.append(item)
    
    def dequeue(self):
        if not self.queue:
            raise Exception("Queue is empty")
        return self.queue.pop(0)
    
    def get_max_length(self):
        return self.max_length
    
    def get_length(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return self.max_length is not None and len(self.queue) >= self.max_length
