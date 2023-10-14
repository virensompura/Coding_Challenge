array = []

n = int(input("Please enter the number of the element of the array: "))

for i in range(n):
    element = int(input(f"Please enter the element {i + 1}: "))
    array.append(element)
    
print("The Final Array before sorting: ", array)

for j in range(len(array) - 1):
    temp = array[j]
    array[j] = array[j + 1]
    array[j + 1] = temp
    
            
print("The sorted array: ",array)

# Output: 
# Please enter the number of the element of the array: 3
# Please enter the element 1: 6
# Please enter the element 2: 2
# Please enter the element 3: 5
# The Final Array before sorting: [6, 2, 5]
# The sorted array:  [2, 5, 6]