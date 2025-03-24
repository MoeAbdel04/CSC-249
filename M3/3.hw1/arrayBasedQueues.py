from ArrayQueue import ArrayQueue

# Make two queues, one bounded to 4 items and the other unbounded
boundedQueue = ArrayQueue(4)
unboundedQueue = ArrayQueue()

# Enqueue 8 items in each queue, handling full queue exception
print("Enqueueing values 1 through 8 to each queue")
for i in range(1, 9):
    try:
        boundedQueue.enqueue(i)
    except Exception as e:
        print(f"  Error enqueueing {i} to bounded queue: {e}")
    unboundedQueue.enqueue(i)

# Dequeue two items from each queue
print("Dequeuing twice")
for _ in range(2):
    print(f"  Dequeued {boundedQueue.dequeue()} from bounded queue")
    print(f"  Dequeued {unboundedQueue.dequeue()} from unbounded queue")

# Enqueue 4 more items
print("Enqueueing values: 10, 20, 30 and 40")
for item in [10, 20, 30, 40]:
    try:
        boundedQueue.enqueue(item)
    except Exception as e:
        print(f"  Error enqueueing {item} to bounded queue: {e}")
    unboundedQueue.enqueue(item)

# Display contents of each queue
print(f"Bounded queue (maxLength={boundedQueue.get_max_length()}) contents:")
while boundedQueue.get_length() > 0:
    print(f"  {boundedQueue.dequeue()}")

print("Unbounded queue contents:")
while unboundedQueue.get_length() > 0:
    print(f"  {unboundedQueue.dequeue()}")
