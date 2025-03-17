class Stack:
    # Initializes the stack.
    # If optional_max_length is omitted or negative, the stack is unbounded.
    # If optional_max_length is non-negative, the stack is bounded.
    def __init__(self, optional_max_length=-1):
        self.stack_list = []
        self.max_length = optional_max_length

    # Pops and returns the stack's top item.
    def pop(self):
        if not self.stack_list:
            raise IndexError("pop from empty stack")
        return self.stack_list.pop()

    # Pushes an item, provided the push doesn't exceed bounds.
    # Returns True if the push occurred, False otherwise.
    def push(self, item):
        if self.max_length >= 0 and len(self.stack_list) == self.max_length:
            return False
        self.stack_list.append(item)
        return True

    # Returns a string representation of the stack.
    def __str__(self):
        return "Stack: " + str(self.stack_list)


def main():
    print("=== Stack Implementation Demo ===")
    print("Select stack type:")
    print("1. Bounded Stack (max length = 3)")
    print("2. Unbounded Stack")
    option = input("Enter option (1 or 2): ")

    if option == '1':
        stack = Stack(3)
        print("\nUsing a bounded stack with max length 3.")
    elif option == '2':
        stack = Stack()
        print("\nUsing an unbounded stack.")
    else:
        print("\nInvalid option. Exiting program.")
        return

    while True:
        print("\nOptions:")
        print("1. Push an item")
        print("2. Pop an item")
        print("3. Display the stack")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to push: ")
            if stack.push(item):
                print(f"Pushed {item} onto the stack.")
            else:
                print("Stack is full. Cannot push item.")
        elif choice == '2':
            try:
                popped_item = stack.pop()
                print(f"Popped item: {popped_item}")
            except IndexError as e:
                print("Error:", e)
        elif choice == '3':
            print(stack)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
