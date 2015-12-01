k = input().split()

a = [1 for i in range(int(k[0]))]
for i in range(int(k[0]), int(k[1]) + 1):
    a.append(0)
    for j in range(i - int(k[0]), i):
        a[i] += int(a[j])
print(a[int(k[1])])



