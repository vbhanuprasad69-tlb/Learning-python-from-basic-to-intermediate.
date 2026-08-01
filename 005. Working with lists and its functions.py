# Few basic codes with lists
Names = ["Kumar", "Ajay" , "Kamal" , "Akshay" ]
print(Names)
print(Names[1])
print(Names[1:])
print(Names[1:3])
Names[1] = "Vikram"
print(Names)

# Using few list functions

#(i) Remove function
Names.remove("Kamal")
print(Names)

#(ii) Append function
Names.append("Kamal")
print(Names)

#(iii) Insert function
Names.insert(4,"Kamal")
print(Names)

#(iv) Finding index of a string
print(Names.index("Kamal"))

#(v) Count function
print(Names.count("Kamal"))

#(vi) Extend function 
Numbers = [56,4,1,6,64,69,8,]
Names.extend(Numbers)
print(Names)

#(vii) Reverse function
Names.reverse()
print(Names)

#(viii) Sort function
print(Numbers)
Numbers.sort()
print(Numbers)

#(ix) Pop function 
Names.pop()
print(Names)

#(x) Clear function
Names.clear()
print(Names)
