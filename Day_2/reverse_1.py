list = []
n = int(input("Please enter the number of the element in list you like to add: "))
for i in range(n):
  element = int(input(f"Please enter the element {i + 1}: "))
  list.append(element)
print("The final list is: ", list)

for i in list:
    list.reverse()
print(list)
