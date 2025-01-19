import numpy as np

def find_cubic_roots():
    print("Cubic Equation: ax^3 + bx^2 + cx + d = 0")
    
    # Take inputs for coefficients
    a = float(input("Enter the coefficient a (for x^3): "))
    if a == 0:
        print("The coefficient 'a' cannot be zero for a cubic equation.")
        return

    b = float(input("Enter the coefficient b (for x^2): "))
    c = float(input("Enter the coefficient c (for x): "))
    d = float(input("Enter the constant term d: "))

    # Coefficients for the cubic equation
    coefficients = [a, b, c, d]

    # Use numpy's roots function to find the roots of the cubic equation
    roots = np.roots(coefficients)

    print("\nThe roots of the cubic equation are:")
    for i, root in enumerate(roots, start=1):
        print(f"Root {i}: {root:.4f}")

# Call the function
find_cubic_roots()