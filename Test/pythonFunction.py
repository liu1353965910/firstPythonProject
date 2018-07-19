# -*- coding: UTF-8 -*-
from collections import deque
from Test import FirstTest

a = 5


def f(n=a):
    """Do nothing, but document it."""
    return n


a = 6
print(f())


list1 = ["a", "b", 1]
list2 = ["a2", "b2", 2]
list1.append("d")
list1.extend(list2)
list1.insert(1, "b3")
list1.remove("a")
list1.pop()
list1.pop(0)
# show = list1.index(1)
#show = list1.count("b")
#show = list1.sort()
#show = list1.reverse()
show = list1[:]
print(show)


queue = deque(["Apple", "Banana", "Cat"])
queue.append("Dog")
queue.append("Egg")
queue.popleft()
queue.popleft()
print(queue)


def make_increment(n):
    """incrementor"""
    return lambda x: x + n


f = make_increment(40)
print(f(1))

print([(x, y) for x in range(10) for y in range(20) if x > y])

t = (1, 2, "a")
print(t)

s1 = {1, 2, 3}
s2 = {1, 3, 4}
print(s1 - s2)
print(s1 ^ s2)
print(s1 | s2)
print(s1 & s2)

dict = {"Apple": 11, "Cat": 33, "Book": 22}
print(dict["Apple"])
print(sorted(list(dict.keys())))
print("Cat" in dict)

for k, v in dict.items():
    print(k, v)


for i, v in enumerate(list1):
    print(i, v)

for q, a in zip(list1, list2):
    print(q, a)

FirstTest.fib(10)
