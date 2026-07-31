# (i) Basic while loop code

i = 0
while i <= 10:
    print(i)
    i = i+1 
# Note that we can write i = i+1 as i += 1 also!

i = 0
while i <= 5:
    print(i)
    i += 1

# (ii) Building a basic screen locking system

Password = "Password@123"
Enter_the_password = input("Enter the password: ")
Trail_count = 0
Trail_limit = 2
out_of_trails = False
while Enter_the_password != Password and not(out_of_trails):
    if Trail_count < Trail_limit:
        print("Incorrect password")
        Enter_the_password = input("Enter the password: ")
        Trail_count += 1
    else:
        out_of_trails = True
if out_of_trails:
    print("3 attempts over try again after 30 seconds ")
else:
    print("Welcome")