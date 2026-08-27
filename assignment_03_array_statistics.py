# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#
def calculate_sum(numbers):
    """Return the sum of all numbers in the list using a loop."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of the numbers."""
    if len(numbers) == 0:
        return 0
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Return the largest number in the list using a loop."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def find_minimum(numbers):
    """Return the smallest number in the list using a loop."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: Number of values must be a positive integer.")
        return

    numbers = []
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)

    print()
    print("Results:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {find_maximum(numbers)}")
    print(f"Minimum: {find_minimum(numbers)}")


if __name__ == "__main__":
    main()

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

