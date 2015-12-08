text = open('en-ru.txt')
ourWords = {}
for line in text:
    line = line.replace(' ', '').replace(',', ' ').replace('.','').replace('  ','').replace('.','').replace('\n', '').split('-')

    ourWords[line[0]]=line[1]
text.close()

EnglishTexT = open('EnglishTest')
