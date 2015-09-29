A = []
for i in range(int(input())):
    A.append(int(input()))
max = A.count(A[0])
K = A[0]
for i in range(len(A)):
    if A.count(A[i]) > max:
        max = A.count(A[i])
        K = A[i]
print(K)
