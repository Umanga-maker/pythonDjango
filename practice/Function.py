def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        user_input = input("Enter a non-negative integer: ")
        number = int(user_input)
        if number < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {number} is {factorial(number)}.")
    except ValueError:
        print("Error: Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()