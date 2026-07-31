# (i) Using for loop in a string

for letter in "My Personal World":
    print(letter)

# (ii) Using for loop in a list

Students = ["Kiran","Parthu","Lakshman","Naveen"]
for Names in Students:
    print(Names)

for index in range(4):
    print(Students[index])

for index in range(len(Students)):
    print(Students[index])

#(iii) Using for loop in range function

for num in range(10):
    print(num)

for index in range(3,20):
    print(index)

#(iv) Using for loop in exponent function

def raise_to_the_power(base_num,power_num):
    result = 1
    for index in range(power_num):
        result = result*base_num
    return result
print(raise_to_the_power(7,3))
        