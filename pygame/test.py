import random

a = [random.randint(0, 5) for i in range(10)]
print(a)
a[0] = -1
print(a)
amount = a.count(-1)
for i in range(len(a)):
    if a[i] == -1:
        for j in range(i, -1, -1):
            a[j] = a[j - 1] 
        for j in range(amount - 2):
            a[j] = random.randint(0, 5)
print(a)