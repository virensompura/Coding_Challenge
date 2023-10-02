test_dic = {}  

n = int(input("Please enter the number of elements in the dictionary: "))

for i in range(n):
    name = input("Please enter the name: ")
    age = int(input("Please enter the age: "))
    test_dic[name] = age  

print("The Dictionary before removing the user data: ", test_dic)

keys_to_remove = [] 

for key in test_dic:
    data_to_remove = input("Please enter the data you want to remove: ")
    keys_to_remove.append(data_to_remove)

for key in keys_to_remove:
    test_dic.pop(key, None)  

print("The Dictionary after removing the user data: ", test_dic)
