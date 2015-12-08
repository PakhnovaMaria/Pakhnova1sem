I = open('input.txt', 'r')
words = I.read()
words = words.replace('.', ' ').replace(',', ' ').replace('?', ' ').replace('!', ' ')
words = words.lower().split(' ')
f={}
for i in words:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

f[''] = 0
Max = words[0]
for i in f:
    if f[i] > f[Max]:
        Max = i

print(Max, f[Max])

for i in f:
    if i != '':
        print(i, f[i])

I.close()
