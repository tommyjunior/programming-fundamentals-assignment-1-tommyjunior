# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols):
    """Read a matrix of size rows x cols from the user."""
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").strip().split()
            if len(row_input) != cols:
                print(f"Please enter exactly {cols} numbers.")
                continue
            try:
                row = [float(x) for x in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return matrix


def print_matrix(matrix):
    """Print a matrix in a neat, aligned grid."""
    if not matrix:
        print("(empty matrix)")
        return
    # Find the widest number for alignment
    max_width = 0
    for row in matrix:
        for val in row:
            max_width = max(max_width, len(f"{val:g}"))
    
    for row in matrix:
        line = "  ".join(f"{val:{max_width}g}" for val in row)
        print(line)


def transpose_matrix(matrix):
    """Return the transpose of the given matrix."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(mat1, mat2):
    """Return the element-wise sum of two matrices of the same size."""
    rows = len(mat1)
    cols = len(mat1[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(mat1[i][j] + mat2[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matA, matB):
    """Return the product of matA (M x N) and matB (N x P)."""
    m = len(matA)
    n = len(matA[0])
    p = len(matB[0])
    
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += matA[i][k] * matB[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def main():
    print("=" * 50)
    print("PART A — Transpose a Matrix")
    print("=" * 50)
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("\nEnter the matrix:")
    matrix = read_matrix(rows, cols)
    
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    
    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transposed)
    
    # ------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("PART B — Add Two Matrices")
    print("=" * 50)
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("\nEnter first matrix:")
    mat1 = read_matrix(rows, cols)
    
    print("\nEnter second matrix:")
    mat2 = read_matrix(rows, cols)
    
    print("\nMatrix 1:")
    print_matrix(mat1)
    print("\nMatrix 2:")
    print_matrix(mat2)
    
    sum_matrix = add_matrices(mat1, mat2)
    print("\nSum of the two matrices:")
    print_matrix(sum_matrix)
    
    # ------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("PART C — Multiply Two Matrices")
    print("=" * 50)
    
    print("\nMatrix A (M x N):")
    m = int(input("Enter number of rows for A: "))
    n = int(input("Enter number of columns for A: "))
    print("Enter matrix A:")
    matA = read_matrix(m, n)
    
    print("\nMatrix B (N x P):")
    print(f"(Number of rows for B must be {n})")
    p = int(input("Enter number of columns for B: "))
    print("Enter matrix B:")
    matB = read_matrix(n, p)   # rows of B must equal columns of A
    
    print("\nMatrix A:")
    print_matrix(matA)
    print("\nMatrix B:")
    print_matrix(matB)
    
    product = multiply_matrices(matA, matB)
    print("\nProduct A × B:")
    print_matrix(product)


if __name__ == "__main__":
    main()

