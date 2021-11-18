def nonDivisibleSubset(S):
    num= [0 for i in range(K)]
    for i in range(N):
        num[S[i] % K] += 1
    if (K % 2 == 0):
        num[K//2] = min(num[K//2], 1)
    num1 = min(num[0], 1)
    for i in range(1,(K // 2) + 1):
        num1 += max(num[i], num[K - i])
    return num1
S= [1,7,2,4]
N = len(S)
K = 3
print(nonDivisibleSubset(S))