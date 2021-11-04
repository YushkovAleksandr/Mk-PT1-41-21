x = ['1', '11', '12', '22', '2', '33', '13', '30']
print(sorted(list(filter(lambda x: int(x) % 2 != 0, x)), key=int))