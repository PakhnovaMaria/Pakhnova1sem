k,n = int(input()), int(input())
a = []
for i in range(0,k):
    a.append(1)
for i in range(k,n+1):
    a.append(0)
    a[i]=int(a[i])
    for j in range(i-k, i):
        a[i]+=int(a[j])
print(a[n])



