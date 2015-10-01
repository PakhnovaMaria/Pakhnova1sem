N = int(input())
A = []
for i in range(N):
    row = input().split()
    for i in range(2):
        row[i] = int(row[i])
    A.append(row)
T = int(input())
n = 0
a = 0
for a in range(N):
    if (A[a][0] <= T) and (A[a][1] >= T):
            n += 1
print(n)


