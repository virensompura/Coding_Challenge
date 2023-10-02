def Merge(test_dict_1, test_dict_2):
    return(test_dict_2.update(test_dict_1))

test_dict_1 = {}

n = int(input("Please enter the number of the element in the dictionary 1: "))

for i in range (n):
    name = input("Please enter the name: ")
    age = int(input("Please enter the age: "))
    test_dict_1[name] = age 

test_dict_2 = {}

m = int(input("Please enter the number of the element in the dictionary 2: "))

for i in range (m):
    name = input("Please enter the name: ")
    age = int(input("Please enter the age: "))
    test_dict_2[name] = age 

print("The Final Dictionary 1 is: ", test_dict_1)
print("The Final Dictionary 2 is: ", test_dict_2)
print(Merge(test_dict_1, test_dict_2))

print("The Merged Dictionary is: ", test_dict_2)
