def binary_search(items, key):
    # Initialize the low and high indices
    low = 0
    high = len(items) - 1
   
    # Loop until low exceeds high
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Compare the middle element with the key
        if items[mid] < key:
            low = mid + 1
        elif items[mid] > key:
            high = mid - 1
        else:
            return mid  # key found at index mid
   
    return -1  # key not found


# Main program to test the binary_search() function   
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
print("WORDS:", words)
     
key = input("Enter a string value: ")
key_index = binary_search(words, key)
     
if key_index == -1:
    print("'{}' was not found.".format(key))
else:
    print("Found '{}' at index {}.".format(key, key_index))
