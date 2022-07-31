#c=, c-, dz=, d-, lj, nj, s=, z=
"""
input_value = input()
input_value = input_value.replace("c=", '1')
input_value = input_value.replace("c-", '1')
input_value = input_value.replace("dz=", '1')
input_value = input_value.replace("d-", '1')
input_value = input_value.replace("lj", '1')
input_value = input_value.replace("nj", '1')
input_value = input_value.replace("s=", '1')
input_value = input_value.replace("z=", '1')
cnt = len(input_value)
print(cnt)
"""
input_value = input()
c_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in c_alphabet:
    input_value = input_value.replace(i, '1')
cnt = len(input_value)
print(cnt)