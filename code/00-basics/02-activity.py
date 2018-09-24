listOfIntegers = range(10)

def isEven(x):
    return x % 2 == 0

for x in listOfIntegers:
    print(x, end='  ')
    if (isEven(x)):
        print("is even")
    else:
        print("is odd")