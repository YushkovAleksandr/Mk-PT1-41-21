from decimal import Decimal

while True:
    try:
        sum_account = Decimal(input("введите сумму счета: ")).quantize(Decimal("1.00"))
        break
    except:
        print("неправильный ввод")

while True:
    try:
        count_party = Decimal(input("введите количество участников: ")).quantize(Decimal("1"))
        break
    except:
        print("неправильный ввод")

while True:
    try:
        sum_party = input("введите суммы участников через пробел, например: 20 30 40: ").split()
        for i in range(len(sum_party)):
            sum_party[i] = Decimal(sum_party[i]).quantize(Decimal("1.00"))
        if len(sum_party) == count_party and sum(sum_party) == sum_account:
            break
        else:
            print("неправильный ввод")
    except:
        print("неправильный ввод")



def debt_counting(sum_account, count_party, sum_party):

    everyone_pays = Decimal(sum_account / count_party).quantize(Decimal("1.00"))
    count_party_dictionary = {}
    sum_plus = {}
    sum_minus = {}

    for i in range(len(sum_party)):
        count_party_dictionary[i+1] = sum_party[i]

    for key, value in count_party_dictionary.items():
        if count_party_dictionary[key] == everyone_pays:
            print(f"участник {key} ничего не должен")
        elif count_party_dictionary[key] < everyone_pays:
            sum_minus[key] = everyone_pays - count_party_dictionary[key]
        else:
            sum_plus[key] = count_party_dictionary[key] - everyone_pays
        
    for sum_plus_key, sum_plus_value in sum_plus.items(): 
        for sum_minus_key, sum_minus_value in sum_minus.items(): 
            if sum_plus_value >= sum_minus_value:
                sum_plus_value -= sum_minus_value
                print(f"участник {sum_minus_key} должен участнику {sum_plus_key}: {sum_minus_value} рублей")
            elif sum_plus_value < sum_minus_value:
                sum_minus_value -= sum_plus_value
                sum_minus[sum_minus_key] = sum_minus_value
                print(f"участник {sum_minus_key} должен участнику {sum_plus_key}: {sum_plus_value} рублей")
                break


debt_counting(sum_account, count_party, sum_party)