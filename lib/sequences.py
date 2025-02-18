#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle edge case if length <= 0
    if length <= 0:
        print("[]")
        return
    
    # Base cases
    fibonacci = [0, 1]
    
    # Generate Fibonacci sequence up to the length-th number
    for i in range(2, length):
        next_fib = fibonacci[-1] + fibonacci[-2]  # Sum of the last two elements
        fibonacci.append(next_fib)
    
    print(fibonacci[:length])  # Print only the first 'length' numbers



