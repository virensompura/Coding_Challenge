
dict = {}


n = int(input("Please enter the number of elements in the dictionary: "))

for i in range(n):
    x = int(input("Please enter the value for x in element {}: ".format(i+1)))
    y = int(input("Please enter the value for y in element {}: ".format(i+1)))
    z = int(input("Please enter the value for z in element {}: ".format(i+1)))
    dict[x, y, z] = x + y - z

# print the dictionary
print(dict)