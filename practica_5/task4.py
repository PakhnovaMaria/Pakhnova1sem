A = input().split()
A = [int(x) for x in A]
for i in range (0, len(A) - len(A)%2, 2):
    A[i], A[i + 1] = A[i + 1], A [i]
print(A)




