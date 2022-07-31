input = int(input())
count = 0
n = 666

while 1:
	if "666" in str(n):
		count += 1
	if count == input:
		break
	n += 1
print(n)

# input = int(input())
# count = 0
# n = 666

# while 1:
# 	num_count = 0
# 	for i in str(n):
# 		if i == "6":
# 			num_count += 1
# 		else:
# 			num_count = 0
# 		if num_count == 3:
# 			count += 1
# 			break
# 	if count == input:
# 		break
# 	n += 1
# print(n)