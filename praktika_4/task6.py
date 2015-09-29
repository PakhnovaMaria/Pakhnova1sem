import robot
# создаем робота
r = robot.rmap()
#загружаем карту соотвествующей задачи
r.lm('task6')

N=int(input())
A=int(input())

def task():
    for n in range (0, A):
        r. pt()
        r. rt(1)
    for I in range (0,A//2+1):
        r. lt(1) 
    for m in range (0, N-1):
        r.dn (1)
        r. pt()

r. start(task)
