import random

T = 100000
print(T)
for _ in range(T):
	print(random.randint(1,2**64 - 1))
