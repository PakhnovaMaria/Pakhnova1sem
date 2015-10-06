input = open('float_data.txt', 'r')
mas = input.read().split()
numbers = list(map(float, mas))
Avg = sum(numbers)/len(numbers)
print(Avg)
A = 0
for i in range(len(numbers)):
    A += (numbers[i] - Avg)**2
Sr = (A / len(numbers)) ** 0.5
print(Sr)
Max = max(numbers)
Min = min(numbers)
print(Max, Min, numbers.index(Max), numbers.index(Min))






