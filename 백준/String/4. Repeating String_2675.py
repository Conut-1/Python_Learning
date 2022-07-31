test_case = int(input())
for i in range(test_case):
    result = ""
    input_value = input().split()
    for cha in input_value[1]:
        result += cha * int(input_value[0])
    print(result)