T = int(input())
for _ in range(T):
    L = True
    N = int(input())
    while(N != 1):
        bits = list(bin(N)[2:])
        if N % 2 == 0:
            N = N // 2
        else:
            bits[bits.index('1', bits.index('1'))] = '0'
            N = int(''.join(bits), 2)
        L = not L
    if not L:
        print("BUELL")
    else:
        print("FENNER")
