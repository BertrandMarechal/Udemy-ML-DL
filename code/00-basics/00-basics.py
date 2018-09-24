listOfNumbers = [1,2,3,4,5,6,7,8,9]

for number in listOfNumbers:
    if (number % 2 ==0):
        print(number,"is even")
    else:
        print(number,"is odd")
print("all done.")


import numpy as np
A = np.random.normal(25.0,  5.0, 10)
print(A)

x = [1,2,3,4,5]
print(len(x))
print(x[:3])
print(x[3:])
x.extend([6,7])
print(x[-2:])
x.append(8)

y = [9, 10, 11]
listOfLists = [x, y]
print(listOfLists)

x = [1,5,9,72,4,3,4,8]
x.sort()
print(x)

(age, income) = "12,123456".split(",")
print(age, income)


dico = {}
dico["age"] = 12
dico["income"] = 123456

print(dico)
print(dico["age"])
print(dico.get("city"))
# print(dico["city"])
for prop in dico:
    print("prop", prop, dico[prop])
