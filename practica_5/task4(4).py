_author__ = 'student'
A = input().split()
A = [int(x) for x in A]

max = 0
for i in range(len(A)):
    if A.count(A[i]) > max:
        max = A.count(A[i])
print(A[i])