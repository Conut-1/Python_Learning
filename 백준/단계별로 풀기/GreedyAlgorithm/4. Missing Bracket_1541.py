equation = input()

eq1, eq2 = (equation + '-0').split('-', 1)
el1 = list(map(int, eq1.split('+')))
el2 = list(map(int, eq2.replace('-', '+').split('+')))
res = sum(el1) - sum(el2)

print(res)
