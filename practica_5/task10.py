numbers, N = list(map(int, input().split())), int(input())
for i in range(N):
    numbers = numbers[0:-1-numbers[-1]]+[numbers[-1]]+numbers[-1-numbers[-1]:-1]
print(' '.join([str(i) for i in numbers]))

