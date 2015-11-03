I = open('input.txt', 'r')
words = I.read()
words = words.replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ')
words = words.lower()
max = 1
for x in words:
    i = words.count(x)
    if i > max:
        max = i
        a = x
print(a)
print(words)
I.close()
