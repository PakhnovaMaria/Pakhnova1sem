A = []
for i in range(int(input())):
    A.append(int(input()))
for i in range(len(A)):
    if A.count(A[i]) == 1:
        print(A[i])