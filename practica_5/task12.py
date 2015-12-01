N = int(input())
A = input().split()
A = [int(x) for x in A]
i = 0
while i < (N-1):
    K = min(A[i::1])
    j = A.index(K)
    A[i], A[j] = A[j], A[i]
    i += 1
print(A[N//2])

