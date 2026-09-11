#nested for loops introduction
cols=5
rows=4
for i in range(rows):
    for i in range(cols):
        print("*", end="")
    print()#print nothing, but go to new line
