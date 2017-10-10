(N, K) = list(map(int, input().split(' ')))
ns = [(0,0,0)] * N
for x in range(N):
        ns[x] = tuple(map(int, input().split(',')))

ks = [(0,0,0)] * K
for x in range(K):
	ks[x] = tuple(map(int, input().split(',')))

def dist_squared_3(A, B):
        return (A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2

ambiguous = []

for x in range(K):
	color = ks[x]
	guess = ns[0]
	guess_dist = dist_squared_3(color, guess)
	for y in range(N):
		base = ns[y]
		base_dist = dist_squared_3(color, base)
		if base_dist < guess_dist:	
			guess = base
			guess_dist = base_dist
	num_closest = 0
	for y in range(N):
		base = ns[y]
		base_dist = dist_squared_3(color, base)
		if base_dist == guess_dist:
			num_closest += 1
	if num_closest > 1:
		ambiguous.append(x)

print(str(N) + " " + str(K-len(ambiguous)))

for x in range(N):
	print(",".join(list(map(str, ns[x]))))

am_idx = 0
for x in range(K):
	if x == ambiguous[am_idx]:
		am_idx += 1
		# Lazy way to prevent index out of range
		am_idx %= len(ambiguous)
		continue
	print(",".join(list(map(str, ks[x]))))
