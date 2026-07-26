num1 = float(input("Enter he first number: "))
OP = input("Enter the operator: ")
num2 = float(input("Enter the second number "))
if OP == "+":
    print(num1+num2)
elif OP == "-":
    print(num1-num2)
elif OP == "*":
    print(num1*num2)
elif OP == "/":
    print(num1/num2)
else:
    print("Invalid")