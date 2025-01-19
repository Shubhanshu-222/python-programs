import numpy as np

# Coefficient matrix
A = np.array([
    [2, -4, -1],
    [4, -8, 3],
    [-2, -4, -1]
])

# Constant vector
b = np.array([-8, 4, 11])

# Check determinant to ensure matrix is invertible
det_A = np.linalg.det(A)
print(f"Determinant of A: {det_A}")

# Solve using inverse matrix method
try:
    # Calculate inverse of A
    A_inv = np.linalg.inv(A)
    
    # Solve x = A^(-1) * b
    x = A_inv @ b
    
    print("\nSolution:")
    print(f"x1 = {x[0]:.4f}")
    print(f"x2 = {x[1]:.4f}")
    print(f"x3 = {x[2]:.4f}")
    
    # Verify the solution
    print("\nVerification:")
    print("Original equations:")
    print(f"2x1 - 4x2 - x3 = {2*x[0] - 4*x[1] - x[2]:.4f}")
    print(f"4x1 - 8x2 + 3x3 = {4*x[0] - 8*x[1] + 3*x[2]:.4f}")
    print(f"-2x1 - 4x2 - x3 = {-2*x[0] - 4*x[1] - x[2]:.4f}")

except np.linalg.LinAlgError:
    print("Matrix is not invertible.")