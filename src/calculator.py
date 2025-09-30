"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result

def power(a, b):
    """Raise a to the power of b without using built-in functions"""
    if not isinstance(a, (int, float)) or not isinstance(b, int):
        raise TypeError("Base must be int/float and exponent must be int")
    if b == 0:
        return 1
    result = 1
    exp = abs(b)
    for _ in range(exp):
        result *= a
    return result if b > 0 else 1 / result

def sqrt(n):
    """Calculate square root using Newton's method"""
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    if n == 0:
        return 0
    guess = n / 2
    for _ in range(20):
        guess = (guess + n / guess) / 2
    return guess



# TODO: Students will add multiply, divide, power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")