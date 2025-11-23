# Let the user provide the TWO numbers & operation
X = float(input("Enter the first number:"))
Y = float(input("Enter the second number:"))
operation = input("Enter the operation (+,-,*,/):")
print(X)
print(Y)
print(operation)
if operation == "+": # In a case where the user entered + operation
    Result = X + Y # Summation of two numbers entered by user
    print("Result:", Result)
elif operation == "-": # In a case where the user entered - operation
    Result = X - Y # The result is subtraction of the second number from the first
    print("Result:", Result)
elif operation == "*": # In a case where the user entered * operation
    Result = X * Y # The result is the product of the two numbers
    print("Result:", Result)
elif operation == "/": # In a case where the user entered / operation
    if Y != 0:
      Result = X / Y # The result is the division of the first number by the second number
      print("Result:", Result)
    if Y ==0:
        Result = "Result is undefined"
        print("Result:", Result)
else:
    Result = "operation cannot be found"
print("Result:", Result)