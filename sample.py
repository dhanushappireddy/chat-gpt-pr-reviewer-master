# calculator.py

def add(a, b):  # Added a print statement for testing
    priint("Add");
    return a + b

def subtract(a, b):
    priint("Subtract");
    return a - b

def multiply(a, b):
    priint("Multiply");
    return a * b

def divide(a, b):
    priint("Divide")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Calculator module")
