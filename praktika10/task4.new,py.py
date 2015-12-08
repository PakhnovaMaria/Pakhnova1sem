__author__ = 'student'
text = open('en-ru.txt')
ourWords = {}
for line in text:
    line = line.replace(' ', '').replace(',', ' ').replace('.', '').replace('  ', '').replace('.', '').replace('\n', '').split('-')

    ourWords[line[0]] = line[1]
text.close()

input = open('input2.txt', 'r')
output = open('output.txt', 'w')
trans = []
for line in input.read():
    line = line.replace('.', '').replace(',', ' ')
    line = line.lower()
    for word in line:
        if word in ourWords:
            trans.append(ourWords[word])
        else:
            trans.append(line)

i = 0
for elem in trans:
    print(elem, end=' ')
    i += 1
    if i % 10 == 0:
        print(elem, end='\n')
        i += 1
    output.write(elem)
    output.write(' ')
output.close()
input.close()
