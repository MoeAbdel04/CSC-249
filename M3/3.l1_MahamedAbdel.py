class Stack:
    # Initializes the stack. If the optional_max_length argument is omitted or 
    # negative, the stack is unbounded. If optional_max_length is non-negative, 
    # the stack is bounded.
    def __init__(self, optional_max_length=-1):
        self.stack_list = []
        self.max_length = optional_max_length

    # Pops and returns the stack's top item.
    def pop(self):
        if not self.stack_list:
            raise IndexError("pop from empty stack")
        return self.stack_list.pop()

    # Pushes an item, provided the push doesn't exceed bounds.
    # Does nothing otherwise. Returns True if the push occurred, False otherwise.
    def push(self, item):
        # If max_length is non-negative (bounded stack) and at max capacity, return False.
        if self.max_length >= 0 and len(self.stack_list) == self.max_length:
            return False
        self.stack_list.append(item)
        return True

# Example usage:
if __name__ == "__main__":
    # Demonstrate a bounded stack with a maximum length of 3.
    print("Bounded Stack (max_length = 3):")
    bounded_stack = Stack(3)
    print("Pushing 1:", bounded_stack.push(1))  # Expected True
    print("Pushing 2:", bounded_stack.push(2))  # Expected True
    print("Pushing 3:", bounded_stack.push(3))  # Expected True
    print("Attempting to push 4 (should fail):", bounded_stack.push(4))  # Expected False

    print("Popping item (should be 3):", bounded_stack.pop())  # Expected 3
    print("Popping item (should be 2):", bounded_stack.pop())  # Expected 2
    print("Popping item (should be 1):", bounded_stack.pop())  # Expected 1

    try:
        print("Attempting to pop from empty stack:")
        bounded_stack.pop()  # This will raise an exception.
    except IndexError as e:
        print("Caught exception:", e)

    print("\nUnbounded Stack:")
    # Demonstrate an unbounded stack (by using the default parameter).
    unbounded_stack = Stack()
    print("Pushing 'a':", unbounded_stack.push("a"))
    print("Pushing 'b':", unbounded_stack.push("b"))
    print("Pushing 'c':", unbounded_stack.push("c"))
    print("Popping item (should be 'c'):", unbounded_stack.pop())
    print("Popping item (should be 'b'):", unbounded_stack.pop())
    print("Popping item (should be 'a'):", unbounded_stack.pop())
