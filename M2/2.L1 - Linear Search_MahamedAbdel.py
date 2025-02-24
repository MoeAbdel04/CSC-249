def linear_search(strings, key):
    for i in range(len(strings)):
        if strings[i] == key:
            return i
    return -1  # not found

# Main program to test the linear_search() method   
strings = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
print("STRINGS:", strings)

key = input("Enter a string value: ")
key_index = linear_search(strings, key)

if key_index == -1:
    print("'{}' was not found.".format(key))
else:
    print("Found '{}' at index {}.".format(key, key_index))
