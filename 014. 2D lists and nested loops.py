number_grid = [[1,2,3],
               [4,5,6],
               [7,8,9],
               [0]   ]

#(i) Locating a specific number
print(number_grid [0][0])
print(number_grid [1][1])

#(ii) Printing all the numbers in a row
for row in number_grid:
    print(row)

#(iii) Printing all the numbers in a column
for col in number_grid:
    print(col)

#(iv) Printing all the numbers from number_grid to row and row to column
for row in number_grid:
    for col in row:
        print(col)

#(v) Printing all the numbers from number_grid to column and column to row
for col in number_grid:
    for row in col:
        print(row)
