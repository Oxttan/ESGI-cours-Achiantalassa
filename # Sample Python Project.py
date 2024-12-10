# Sample Python Project

def greet(name):
    """Function to greet a user by name."""
    return f"Hello, {name}!"

def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

def main():
    """Main function to demonstrate functionality."""
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 7 = {subtract(10, 7)}")

if __name__ == "__main__":
    main()