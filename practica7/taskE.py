import matplotlib.pyplot as plt

stdin=open('input.txt')
text=stdin.read()
words=['']
alphabet=''.join([chr(i) for i in range(ord('a'), ord('z')+1)]) + ''.join([chr(i) for i in range(ord('а'), ord('я')+1)])
for i in text:
	if i.lower() not in alphabet and words[-1] != '':
		words+=['']
	elif i.lower() in alphabet:
		words[-1] += i
if '' in words: words.remove('')
words.sort(key=len)
frequency = [0 for i in range(len(words[-1]))]
xs = [i for i in range(1, len(words[-1]) + 1)]
for i in words:	
	frequency[len(i) - 1] += 1
plt.bar(xs, frequency)
plt.show()