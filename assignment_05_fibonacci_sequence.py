# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_fibonacci(n):
    """Print the first n terms of the Fibonacci sequence."""
    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
        return

    a, b = 0, 1
    print("Fibonacci sequence:", end=" ")
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()   # new line at the end


def is_fibonacci(num):
    """Return True if num is a Fibonacci number, otherwise False."""
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num


def main():
    # ---------- PART A ----------
    print("=" * 40)
    print("PART A — Print the First N Terms")
    print("=" * 40)
    
    n = int(input("How many terms? "))
    print_fibonacci(n)

    # ---------- PART B ----------
    print("\n" + "=" * 40)
    print("PART B — Check if a Number Belongs to the Sequence")
    print("=" * 40)
    
    number = int(input("Enter a number to check: "))
    
    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()

