#Basic string codes
print("LIon Club")

print("Lion Club is\nvery cool")

print('Lion\'Club')

#Trying different functions
#(i) Storing a srting in another string
Club='Lion Club'
print(Club)

#(ii) Joining two strings 
print(Club + " is very good")

#(iii) Using upper()
print(Club.upper())

#(iv) Using lower()
print(Club.lower())

#(v) Using "is" function to know whether a function is true or false
print(Club.islower())

#(vi) Using two functios at a time 
print(Club.upper().isupper())

#(vii) Using len() to know the lenth of a character
print(len(Club))

#(viii) Finding a character by its index number, where Club="Lion Club"
#                                                            012345678
print(Club[1])
print(Club[4])

#(ix) Finding an index number by its character, where Club="Lion Club"
#                                                           012345678
print(Club.index("u"))

#(x) Replacing a string with another string
print(Club.replace("Lion","Elephant"))
