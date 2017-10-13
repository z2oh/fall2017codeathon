import random

N = int(10e5)
mi = 1
ma = int(1e10)
print(str(N))
for _ in range(N):
	print(' '.join(list(map(str, [random.randint(mi, ma), random.randint(mi, ma), random.randint(mi, ma)]))))
