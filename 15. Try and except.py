# Using try and except block
#(i) Simple way to use try and wxcept block
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Inalid input")

#(ii) Using zero division error
try:
    value = 10/0
except ZeroDivisionError as err:
    print(err)

#(iii) Using value error
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print(err)