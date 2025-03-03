def factorial_iterative(n):
    """Computes factorial iteratively."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Computes factorial recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def fibonacci_iterative(n):
    """Computes Fibonacci number iteratively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    """Computes Fibonacci number recursively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    num = 6  # You can change this value to test different numbers
    
    print(f"Factorial of {num} (Iterative):", factorial_iterative(num))
    print(f"Factorial of {num} (Recursive):", factorial_recursive(num))

    print(f"Fibonacci of {num} (Iterative):", fibonacci_iterative(num))
    print(f"Fibonacci of {num} (Recursive):", fibonacci_recursive(num))
