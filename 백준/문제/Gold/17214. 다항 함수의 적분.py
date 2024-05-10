import re

expression = input()
terms = re.findall("(-[0-9]*x*|[0-9]+x*|[0-9]*x+)", expression)

res = []
for i, term in enumerate(terms):
    try:
        start = term.index("x")
    except:
        start = len(term)
    degree = len(term) - start
    coefficient = int(term[:start])
    if coefficient == 0:
        continue
    if coefficient < 0:
        res.append("-")
    if coefficient > 0 and i != 0:
        res.append("+")
    new_term = ""
    if abs(coefficient // (degree + 1)) != 1:
        new_term += str(abs(coefficient // (degree + 1)))
    new_term += "x" * (degree + 1)
    res.append(new_term)

if len(res):
    res.append("+")
res.append("W")

print("".join(res))
