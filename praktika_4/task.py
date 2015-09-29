import robot
# создаем робота
r = robot.rmap()
#загружаем карту соотвествующей задачи
r.lm('task1')
def task():
    r. up(1)
    r. rt (1)
    r. dn(1)
    r. rt (1)
    r. up (1)
    r. rt (1)
    r. dn (1)    
r.start(task)
