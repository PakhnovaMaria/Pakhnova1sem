f = open('input.txt')
N = int(f.readline())
A = f. readline().split()
for i in range(len(A)):
    A[i] = int(A[i])

for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        if A[i] == A[j]:
            x = A[i]

f = open('output. txt', 'w')
print(x, file = f)
f. close()