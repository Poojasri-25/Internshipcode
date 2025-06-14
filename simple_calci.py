# Simple Calculator Program

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation =input("Choose an operation: \n1. Addition (+) \n2. Subtraction (-) \n3. Multiplication (*) \n4. Division (/) \n Enter the operation (1/2/3/4 or +, -, *, /): \n\n")

# calculation based on user input
if operation == '1' or operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '2' or operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '3' or operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '4' or operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
