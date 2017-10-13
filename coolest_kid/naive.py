A = list(range(int(input())))

ind = 1
while(len(A) != 1):
	del A[ind]
	ind+=1
	if(ind >= len(A)):
		ind %= len(A)

print(A[0] + 1)