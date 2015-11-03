I = open('input.txt', 'r')
words = I.read()
words = words.replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ')
words = words.lower().split(' ')
f={}
for i in words:
    if i in f:
        f[i]+=1
    else:
        f[i]=1

f['']=0
max=words[0]
for i in f:
    if f[i]>f[max]: max=i

print(max, f[max])

for i in f:
    if i!='':
        print(i, f[i])

I.close()
