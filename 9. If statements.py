# (i) Basic if statements
# Case 1
is_Good_Climate = True 
if is_Good_Climate:
    print("Lets go for a trip")
else:
    print("Lets go for watching a movie")    

#Case 2
is_Good_Climate = False 
if is_Good_Climate:
    print("Lets go for a trip")
else:
    print("Lets go for watching a movie")

# (ii) Using "or" in if statements 
#case 1
is_Good_Climate = True
is_You_are_free = True 
if is_Good_Climate or is_You_are_free:
    print("Lets go for a trip")
else:
    print("Lets work on our project")

#Case 2
is_Good_Climate = True
is_You_are_free = False 
if is_Good_Climate or is_You_are_free:
    print("Lets go for a trip")
else:
    print("Lets work on our project")

#Case 3
is_Good_Climate = False
is_You_are_free = True 
if is_Good_Climate or is_You_are_free:
    print("Lets go for a trip")
else:
    print("Lets work on our project")

#Case 4
is_Good_Climate = False
is_You_are_free = False 
if is_Good_Climate or is_You_are_free:
    print("Lets go for a trip")
else:
    print("Lets work on our project")

# (iii) Using "and" and "not" in if statements
#Case 1
is_Good_Climate = True
is_You_are_free = True 
if is_Good_Climate and is_You_are_free:
    print("Lets go for a trip and also lets watch any movie ")
elif is_Good_Climate and not(is_You_are_free):
    print("Lets go for a trip")
elif not(is_Good_Climate) and is_You_are_free:
    print("Lets watch any movie")
else:
    print("Lets work on our project")

#Case 2
is_Good_Climate = True
is_You_are_free = False
if is_Good_Climate and is_You_are_free:
    print("Lets go for a trip and also lets watch any movie ")
elif is_Good_Climate and not(is_You_are_free):
    print("Lets go for a trip")
elif not(is_Good_Climate) and is_You_are_free:
    print("Lets watch any movie")
else:
    print("Lets work on our project")

#Case 3
is_Good_Climate = False
is_You_are_free = True
if is_Good_Climate and is_You_are_free:
    print("Lets go for a trip and also lets watch any movie ")
elif is_Good_Climate and not(is_You_are_free):
    print("Lets go for a trip")
elif not(is_Good_Climate) and is_You_are_free:
    print("Lets watch any movie")
else:
    print("Lets work on our project")

#Case 4
is_Good_Climate = False
is_You_are_free = False
if is_Good_Climate and is_You_are_free:
    print("Lets go for a trip and also lets watch any movie ")
elif is_Good_Climate and not(is_You_are_free):
    print("Lets go for a trip")
elif not(is_Good_Climate) and is_You_are_free:
    print("Lets watch any movie")
else:
    print("Lets work on our project")

# (iv) Doing camparisions in if statements to find the greatest or least number

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(565,-4885,25))   