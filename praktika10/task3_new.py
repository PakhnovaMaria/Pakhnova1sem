I = open('input.txt', 'r')
words = []
for a in I.read().split():
    words.append(a)
B = {}
for b in words:
    B[(b)] = words.count(b)
print(B)
I.close()