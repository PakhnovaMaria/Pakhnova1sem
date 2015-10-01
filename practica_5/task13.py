A = input().split()
for i in range(10):
    A[i] = int(A[i])
i = 0
d = 0
while i < 9:
    if A[i] == 2:
        if A[i+1] > 2:
            d += 1
    i += 1
print(int((((sum(A) - (2 * d))/(10-d))*10//10)))
