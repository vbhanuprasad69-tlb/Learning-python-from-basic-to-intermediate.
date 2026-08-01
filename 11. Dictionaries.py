Students_roll_numbers = {
    1: "Abhishek",
    2: "Ajay",
    3: "Akhil",
    4: "Bhanu",
    5: "Bhuvan",
    6: "Chandan",
    7: "Deepak",
    8: "Jagan",
    9: "Kiran",
    10: "Lokesh",
    11: "Mangapathi",
    12: "Naveen",
    13: "Praveen",
    14: "Rohit",
    15: "Sevanth",
    16: "Vasanth",
    17: "Yeshwanth"}

print(Students_roll_numbers[17])
print(Students_roll_numbers[12])
print(Students_roll_numbers.get(6))
print(Students_roll_numbers.get(8,"Invalid roll number"))
print(Students_roll_numbers.get(20,"Invalid roll number"))

#(i) Using update() to change to add new key-value pairs
Students_roll_numbers.update({18:"Yogesh"})
print(Students_roll_numbers[18])

#(ii) Using pop() to remove a specific key and return the value
Students_roll_numbers.pop(17)
print(Students_roll_numbers.get(17,"Invalid roll number"))

#(iii) Using key() to print all the keys stored in the dictionary
all_keys = Students_roll_numbers.keys()
print(all_keys)

for names in Students_roll_numbers.keys():
    print(names)

#(iv) Using values() to print all the values stored in the dictionary
all_values = Students_roll_numbers.values()
print(all_values)

for names in Students_roll_numbers.values():
    print(names)

#(v) Using items() to print all the items stored in the dictionary
all_items = Students_roll_numbers.items()
print(all_items)

for details in Students_roll_numbers.items():
    print(details)

for roll_num,name in Students_roll_numbers.items():
    print(roll_num,name)
