input = open('int_data.txt', 'r')
numbers = list(map(float, input.read().split()))
counts = {num: numbers.count(num) for num in set(numbers)}
max = numbers[0]
min = numbers[0]
for num in set(numbers):
    if counts[num] > counts[max]:
        max = num
    if counts[num] < counts[min]:
        min = num
print(max, min)
print(len(set(numbers)))
