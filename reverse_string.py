str = input("Please enter the string: ").split()[::-1]
l = []

for i in str:
   l.append(i)
print(" ".join(l))
