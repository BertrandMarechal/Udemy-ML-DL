def square(x):
    return x * x
def doSomething(f, x):
    return f(x)

print(square(2))
print(doSomething(square, 2))
print(doSomething(lambda x: x * x * x, 10))

print(2 == 3)
print(True or False)
print(True and False)

if 1 is 3:
    print("WTF")
elif 1 > 3:
    print("impossible")
else:
    print("ok")

for x in range(10):
    print(x)

for x in range(10):
    if (x is 1):
        continue
    if (x > 5):
        break
    print(x)

x = 0

while (x < 10):
    print(x)
    x += 1

