# -*- coding: UTF-8 -*-

1+1
print(1+1)
print(7/3)
print(7//3)
a = 10
b = 20
c = 30
print(a+b)
print(int(7.33))
print(r"'abc\
a\
''")
print("a"*5+"b"*5)
print("a""b")
print("abc".strip("a"))
str = "abcdefg"
print(str[0:1])
print(str[0:])
print(str[:])
print(str[4])
print(str[4:10])
print(str[-1])
print(len(str))
print(str+"\u0020"+str[4])
print(str.encode("UTF-8"))

a = ["a", 100, "abc"]
print(a[0])
print(a[1:])
print(a[:])
a[1] = a[1]+1
print(a)
a[1:1] = [20]
print(a)
a[0:1] = []
print(a)
print(len(a))
b = ["b", 200, "bcd"]
c = [a, b]
print(c)
print(c[1][2])
c.append(300)
print(c)

# fibonacci series:
d, e = 0, 1
while e < 10:
    print(e, end=" ")
    d, e = e, d+e

f = int(input("请输入一个整数："))
if f < 10:
    print("该数小于10")
elif f > 10 & f < 100:
    print("该数大于10且小于100")
else:
    print("else number")

for x in b[:]:
    print(x)

for g in range(20):
    print(g, end=" ")

for g in range(10, 20):
    print(g, end=" ")

for g in range(10, 20, 3):
    print(g, end=" ")

for g in range(2, 10):
    for x in range(2, g):
        if g % x == 0:
            print(g, "equals", x, "*", g//x)
            break
    else:
        print(g, "is a prime number!")
else:
    print("1111")


def fib(n):
    """ This is fibonacci series up to n"""
    a1, b1 = 0, 1
    while a1 < n:
        print(a1, end=" ")
        a1, b1 = b1, a1+b1


fib(100)
















