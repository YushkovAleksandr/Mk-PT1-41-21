# 3. Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

while True:
    try:
        y = int(input('Введите количество чисел для отображения: ')) + 1
        break  
    except:
        print('Данные введены неккоректно')
        continue

def fib(x):
    if x==1:
        return 0
    if x==2:
        return 1
    return fib(x-1)+fib(x-2)

def a(c):
    s = []
    for i in range(1,c):
        b = fib(i)
        s.append(b)
    return (', '.join(map(str,s))) 

print(a(y))