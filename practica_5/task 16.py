N = int(input())
A = [[1]]
for j in range(1,N+1):
    l = [0] + A[j-1]
    r = A[j-1] + [0]
    row = [l[i]+r[i] for i in range(j+1)]
    A += [row]
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = str(A[i][j])
    A[i] = ' '.join(A[i])
    print(A[i])


