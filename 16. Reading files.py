#(i) Checking wheather a file is readable or writable
employee_file = open("Employees1.txt","r")
print(employee_file.readable())

employee_file = open("Employees1.txt","w")
print(employee_file.writable())

employee_file = open("Employees1.txt","r")
print(employee_file.writable())

employee_file = open("Employees1.txt","w")
print(employee_file.readable())

#(ii) Opening a text file inside python
employee_file = open("Employees1.txt","r")
print(employee_file.read())

#(iii) Using read line() to read a text file line by line
employee_file = open("Employees1.txt","r")
print(employee_file.readline())
print(employee_file.readline())

#(iv) Using readlines() to read multiple lines 
employee_file = open("Employees1.txt","r")
print(employee_file.readlines())

#(v) Using readlines function to read a specific line the text file
employee_file = open("Employees1.txt","r")
print(employee_file.readlines()[2])

#(vi) Using for loop in the text file
employee_file = open("Employees1.txt","r")
for employee in employee_file.readlines():
    print(employee)


