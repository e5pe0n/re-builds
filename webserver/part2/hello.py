lst1 = [0, 1, 2]
lst2 = [0, 1, 2]


def g():
    lst1[:] = [10, 11]
    lst2 = [10, 11]


g()

print(lst1)  # [10, 11]
print(lst2)  # [0, 1, 2]

lst1 = [0, 1, 2]
lst2 = [0, 1, 2]


def f():
    global lst1
    lst1 = [10, 11]
    lst2 = [10, 11]


f()

print(lst1)  # [10, 11]
print(lst2)  # [0, 1, 2]
