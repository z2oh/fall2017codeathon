import random
n = 5
k = 5
print(str(n) + ' ' + str(k))
for x in range(n):
	color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
	print(",".join(list(map(str, color))))

for x in range(k):
	color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
	print(",".join(list(map(str, color))))
