# Insertion at the beginning in OrderedDict

def Merge(test_dict_1, test_dict_2):
    return(test_dict_2.update(test_dict_1))

test_dict_1 = {}
test_dict_2 = {}
n = int(input("Please enter the element of the dictionary: "))

for i in range(n):
    name_1 = input("Please enter the name: ")
    age_1 = int(input("Please enter the age: "))
    test_dict_1[name_1] = age_1
    
print("The Final Dictionary is: ", test_dict_1)

while(True): 
    element = int(input("Please enter the number of the element want to include(enter 0 to exit): "))
    if element == 0:
        print("Final Dictioary is ", test_dict_1)
        break
    else: 
        for i in range(element):
            name_2 = input("Please enter the name want to update: ")
            age_2 = input("Please enter the age want to update: ")
            test_dict_2[name_2] = age_2

        Merge(test_dict_1, test_dict_2)
        print("The updated dictionary is: ", test_dict_2) 
        break
    