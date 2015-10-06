N = int(input())
A = []
for i in range(N):
    A. append(int(input()))
i = 0
while i < N:
    K = min(A[i::1])
    j = A.index(K)
    A[i], A[j] = A[j], A[i]
    i += 1
print(A[N//2])