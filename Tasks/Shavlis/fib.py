# def fib(x):
#     if x==1:
#         return 0
#     if x==2:
#         return 1
#     return fib(x-1)+fib(x-2)

# def a(c = int(input()) + 1):
#     s = []
#     for i in range(1,c):
#         b = fib(i)
#         s.append(b)
#     return s 

# print(a())

def fib(x):
    if x==1:
        return 0
    if x==2:
        return 1
    return fib(x-1)+fib(x-2)

def a(c = int(input()) + 1):
    s = ''
    for i in range(1,c):
        b = fib(i)
        s += f'{b}, '
    return s 

print(a())