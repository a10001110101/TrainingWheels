n = 0
a = 0
b = 1
c = 0
print(n)

while (n < 10000):
    c = (a + b)
    a = b
    b = c
    n = a
    print(n)
