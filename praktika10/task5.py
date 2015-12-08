Input = open('input3.txt', 'r')
t = {}
for l in Input:
    l = l[:-1].split(' - ')
    l[1] = l[1].split(', ')
    for i in l[1]:
        if i not in t.keys():
            t[i] = [l[0]]
        else:
            t[i].append(l[0])
Input.close()
output = open('output.txt', 'w')
for i in sorted(t.keys()):
    print(i, ' - ', ', '. join(t[i]), file=output)
output.close()