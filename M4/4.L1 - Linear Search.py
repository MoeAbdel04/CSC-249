def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1  # not found


def main():
    # Initialize the list of numbers
    numbers = [2, 4, 7, 10, 11, 32, 45, 87]
    print("NUMBERS: ", end="")
    for num in numbers:
        print(num, end=" ")
    print("\n")  # New line for formatting

    # Ask user for a number to search
    try:
        key = int(input("Enter a value: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Perform linear search
    key_index = linear_search(numbers, key)

    # Display result
    if key_index == -1:
        print(f"{key} was not found.")
    else:
        print(f"Found {key} at index {key_index}.")


# Run the main function
if __name__ == "__main__":
    main()
