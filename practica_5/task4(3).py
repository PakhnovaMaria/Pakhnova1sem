__author__ = 'student'
A = input().split()
A = [int(x) for x in A]

for i in range(len(A)):
    if A.count(A[i]) == 1:
        print(A[i])
