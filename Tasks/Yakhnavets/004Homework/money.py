#2. Написать программу для вычисления суммы долга при расчёте в ресторане.
#  Например, счёт в 150$ делится на троих, участник №1 внёс 100$, двое остальных (№2 и №3) - 15$ и 35$ соответственно. 
#Программа должна оповестить пользователя о том, что участник №2 должен участнику №1 ещё 35$, а участник №3 - ещё 15$.
#Пользователь вводит сумму счёта, количество участников, их суммы.
from decimal import Decimal

full_cash = float(input("Please, input the sum of payment receipt\n"))
how_much = int(input("How much person\n"))
payers = (input("Input the sum of each member (separeted with comma)\n"))
perperson = full_cash/ how_much
people = []
        
def check_in(people):
    for i in payers.split(","):    
        if i == int(i):
            return people                                                            
while True:        
    try:
        check_in(payers)
        break
    except ValueError:
        payers = str(input("Sorry, i couldt anderstand what did you mean\n Try again\n"))
        continue
each_payed = []
for i in payers:
    each_payed.append(i)
    print(i)
credits = {}
debets = {}

def creddebet():
    
    if each_payed[i] < perperson:
        for k,v in debets.items:
            debets[k] = perperson-each_payed[i]
        
print(debets)