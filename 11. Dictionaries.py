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