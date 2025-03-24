from Stack import Stack
from Queue import Queue

def print_stack(stack):
    print('Current Stack:', end=' ')
    node = stack.list.head
    while node:
        print(node.data, end=' ')
        node = node.next
    print()

def print_queue(queue):
    print('Current Queue:', end=' ')
    node = queue.list.head
    while node:
        print(node.data, end=' ')
        node = node.next
    print()

def main():
    num_stack = Stack()
    num_queue = Queue()

    while True:
        print("\nChoose an option:")
        print("1. Push to Stack")
        print("2. Pop from Stack")
        print("3. Enqueue to Queue")
        print("4. Dequeue from Queue")
        print("5. View Stack")
        print("6. View Queue")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to push onto stack: ")
            num_stack.push(item)
            print_stack(num_stack)
        elif choice == '2':
            try:
                popped = num_stack.pop()
                print(f"Popped item: {popped}")
            except Exception as e:
                print(e)
            print_stack(num_stack)
        elif choice == '3':
            item = input("Enter item to enqueue to queue: ")
            num_queue.enqueue(item)
            print_queue(num_queue)
        elif choice == '4':
            try:
                dequeued = num_queue.dequeue()
                print(f"Dequeued item: {dequeued}")
            except Exception as e:
                print(e)
            print_queue(num_queue)
        elif choice == '5':
            print_stack(num_stack)
        elif choice == '6':
            print_queue(num_queue)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
