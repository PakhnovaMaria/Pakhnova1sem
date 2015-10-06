N = int(input())
A = input().split()
for i in range(N):
    A[i] = int(A[i])
k = int(input())
Max = sum(A[0:k])
i = 1
while i <= (N-2):
    if sum(A[i:i+k]) > Max:
        Max = sum(A[i:i+k])
    i += 1
print(Max)